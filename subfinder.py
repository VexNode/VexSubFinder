import requests

# Terminal ranglari
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
ENDC = '\033[0m'

# r""" bu belgilarni Python xato deb o'ylamasligi uchun shart
BANNER = r"""
 __      __             _   _           _      
 \ \    / /            | \ | |         | |     
  \ \  / /  ___ __  __ |  \| |  ___   _| |  ___ 
   \ \/ /  / _ \\ \/ / | . ` | / _ \ / _` | / _ \
    \  /  |  __/ >  <  | |\  || (_) | (_| ||  __/
     \/    \___|/_/\_\ |_| \_| \___/ \__,_| \___|

      >>> VexNode Subdomain Finder v2.0 <<<
      >>> Created by: VexNode           <<<
"""

def find_subdomains():
    print(CYAN + BANNER + ENDC)
    domain = input(f"{GREEN}Target Domain: {ENDC}")
    
    # subdomains.txt faylini o'qib olish
    try:
        with open("subdomains.txt", "r") as f:
            sub_list = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"{RED}[!] subdomains.txt topilmadi!{ENDC}")
        return

    print(f"\n[*] {len(sub_list)} ta subdomen tekshirilmoqda...\n")

    for sub in sub_list:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"{GREEN}[+] Found: {url}{ENDC}")
        except:
            continue

    print(f"\n{CYAN}--- Scan complete. VexNode out. ---{ENDC}")

if __name__ == "__main__":
    find_subdomains()
