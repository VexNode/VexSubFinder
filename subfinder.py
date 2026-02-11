import requests

# Terminal ranglari
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
ENDC = '\033[0m'

BANNER = f"""{CYAN}
__     __          _   _           _      
\ \   / /         | \ | |         | |     
 \ \_/ /__ _  _   |  \| | ___   __| | ___ 
  \   // _ \ \/ / | . ` |/ _ \ / _` |/ _ \
   | ||  __/>  <  | |\  | (_) | (_| |  __/
   |_| \___/_/\_\ |_| \_|\___/ \__,_|\___|
                                          
    {GREEN}>>> VexNode Subdomain Finder v2.0 <<<{CYAN}
    {GREEN}>>> Created by: VexNode           <<<{ENDC}
"""

def find_subdomains():
    print(BANNER)
    domain = input(f"{GREEN}Target Domain (masalan: google.com): {ENDC}")
    
    # Kiber-razvedka uchun eng mashhur subdomenlar lug'ati
    sub_list = [
        "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "ns2",
        "admin", "dev", "test", "api", "staging", "m", "blog", "shop", "support",
        "vpn", "secure", "proxy", "portal", "cloud", "dns", "gateway", "remote",
        "apps", "status", "git", "gitlab", "devops", "cpanel", "whm", "jenkins",
        "jira", "confluence", "internal", "hr", "payroll", "docs", "static",
        "assets", "cdn", "media", "images", "videos", "uploads", "files", "beta",
        "alpha", "demo", "client", "customer", "partner", "manage", "billing",
        "payment", "auth", "login", "register", "signup", "search", "tools",
        "vps", "server", "db", "database", "sql", "monitor", "nagios", "zabbix"
    ]
    # Siz bunga yana yuzlab so'zlarni qo'shishingiz mumkin

    print(f"\n[*] {len(sub_list)} ta subdomen tekshirilmoqda...\n")

    for sub in sub_list:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"{GREEN}[+] Found Active: {url} (Status: 200){ENDC}")
            elif response.status_code == 403:
                print(f"{RED}[!] Found Forbidden: {url} (Status: 403){ENDC}")
        except requests.ConnectionError:
            pass
        except:
            continue

    print(f"\n{CYAN}--- Scan complete. VexNode out. ---{ENDC}")

if __name__ == "__main__":
    find_subdomains()
