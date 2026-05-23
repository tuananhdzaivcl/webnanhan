import requests
import json
import time

def auto_funlink_bypass():
    print("\033[1;32m[+] KHỞI ĐỘNG HỆ THỐNG BYPASS FUNLINK [+]\033[0m")
    
    raw_json_data = '''{
      "data_link": {"id": "PtwrMFI"},
      "data_keyword": {"keyword_text": "789club cricketcarnival.in.net"},
      "ip": "116.106.97.119"
    }'''
    
    data = json.loads(raw_json_data)
    link_id = data['data_link']['id']
    tu_khoa = data['data_keyword']['keyword_text']
    
    print(f"\033[1;36m[*] ID Nhiệm vụ:\033[0m {link_id}")
    print(f"\033[1;36m[*] Từ khóa cần tìm:\033[0m {tu_khoa}")
    time.sleep(3)
    
    ma_xac_nhan = "MA_XAC_NHAN_LAY_DUOC_TU_GOOGLE"
    print(f"\033[1;32m[+] Giả lập mã lấy được:\033[0m {ma_xac_nhan}")
    
    url_api = "https://public.funlink.io/api/verify"
    
    payload = {
        "link_id": link_id,
        "traffic_code": ma_xac_nhan
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
    }
    
    print("\033[1;36m[*] Đang dội bom request lên public.funlink.io...\033[0m")
    
    try:
        response = requests.post(url_api, json=payload, headers=headers)
        
        print(f"\n\033[1;37m[Server Trả Về - Status {response.status_code}]:\033[0m")
        print(response.text)
        
    except Exception as e:
        print(f"\n\033[1;31m[-] Đứt cáp: {e}\033[0m")

if __name__ == "__main__":
    auto_funlink_bypass()

