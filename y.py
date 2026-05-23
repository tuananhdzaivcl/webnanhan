import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuration
HOTMAIL_URL = "https://signup.live.com/"
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

def generate_credentials():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["@outlook.com", "@hotmail.com"])
    email = username + domain
    password = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=12))
    return email, password

def setup_driver():
    chrome_options = Options()
    # Nếu bị chặn, hãy thử bỏ dòng --headless
    # chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def create_hotmail_account(driver, email, password):
    try:
        driver.get(HOTMAIL_URL)
        wait = WebDriverWait(driver, 20)

        # 1. Điền Email
        email_input = wait.until(EC.presence_of_element_located((By.ID, "MemberName")))
        email_input.send_keys(email.split('@')[0])
        driver.find_element(By.ID, "iSignupAction").click()
        
        # 2. Điền Password
        password_input = wait.until(EC.presence_of_element_located((By.ID, "PasswordInput")))
        password_input.send_keys(password)
        driver.find_element(By.ID, "iSignupAction").click()

        # 3. Điền Tên
        first_name = wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        first_name.send_keys("Lo")
        driver.find_element(By.ID, "LastName").send_keys("Manh")
        driver.find_element(By.ID, "iSignupAction").click()

        # 4. Ngày tháng năm sinh (Ví dụ)
        wait.until(EC.presence_of_element_located((By.ID, "BirthDay"))).send_keys("01")
        driver.find_element(By.ID, "BirthMonth").send_keys("January")
        driver.find_element(By.ID, "BirthYear").send_keys("2000")
        driver.find_element(By.ID, "iSignupAction").click()

        print(f"Thành công đến bước cuối cho: {email}")
        
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Lỗi tại bước: {e}")
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")

# Chạy thử
if __name__ == "__main__":
    driver = setup_driver()
    email, password = generate_credentials()
    create_hotmail_account(driver, email, password)
    # driver.quit()
