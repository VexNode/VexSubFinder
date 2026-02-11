import requests

def find_subdomains():
    print("-" * 40)
    print("   VEX-SUBFINDER v2.0 | Professional   ")
    print("-" * 40)
    
    domain = input("Target Domain (masalan: google.com): ")
    
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

    print(f"[*] {len(sub_list)} ta subdomen tekshirilmoqda...")

    for sub in sub_list:
        url = f"http://{sub}.{domain}"
        try:
            # timeout=2 skaner tezroq ishlashi uchun
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print(f"[+] Found Active: {url} (Status: 200)")
            elif response.status_code == 403:
                print(f"[!] Found Forbidden: {url} (Status: 403 - Admin panel bo'lishi mumkin)")
        except requests.ConnectionError:
            pass
        except Exception as e:
            continue

    print("-" * 40)
    print("Scan complete. VexNode out.")

if __name__ == "__main__":
    find_subdomains()
