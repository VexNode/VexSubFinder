import requests

def find_subdomains(domain, wordlist):
    print(f"Searching subdomains for: {domain}...")
    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"[+] Found: {url}")
        except requests.ConnectionError:
            pass

target_domain = input("Enter domain (e.g. google.com): ")
# Oddiy test uchun kichik lug'at
test_words = ["www", "mail", "ftp", "admin", "dev", "test", "api"]

find_subdomains(target_domain, test_words)
