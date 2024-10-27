import subprocess
import sys

# CODES ANSI FOR COLERED THE TERMINAL AND TEXT APRESENTED FOR USER
class colors:
      red = "\033[31m"
      green = "\033[32m"
      blue = "\033[34m"
      cyan = "\033[36m"
      purple = "\033[35m"
      reset = "\033[0m"
      pink = "\033[95m"

      # FORMAT TEXT
      bright = '\033[1m'
      background_green = '\033[32m'
      background_red = '\033[41m'
      blink = '\033[5m'
      sublime = '\033[4m'

      # COLOR + BRIGHT
      sb = f'{bright}{sublime}'
      gb = f'{bright}{green}'
      bb = f'{bright}{blue}'

# FLAGS FOR ALERT THE USER
class flags:
      ok = f'{colors.bright}{colors.green}[ * ]{colors.reset}'
      error = f'{colors.bright}{colors.red}[ * ]{colors.reset}'
      finalization = f'{colors.purple}{colors.bright}[ * ]{colors.reset}'

def extract_img(path):			
    with open(path, "rb") as img:
         path_result = "./steg_result.txt"
         with open(path_result, "w") as file_result:
              try: # stdout=subprocess.PIPE, stderr=subprocess.STDOUT
                 exiftool_results = subprocess.run(['exiftool', '-v', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
                 binwalk_results = subprocess.run(['binwalk', '-v', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
                 strings_results = subprocess.run(['strings', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
                 xxd_results = subprocess.run(['xxd', '-a', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)

                 file_result.write(f"Basic Data:\n{exiftool_results.stdout.decode()}\n")
                 file_result.write(f"Info Image:\n{binwalk_results.stdout.decode()}\n")
                 file_result.write(f"String words found:\n{strings_results.stdout.decode()}\n")
                 file_result.write(f"Hex content:\n{xxd_results.stdout}.decode()")
                  
              except Exception as error:
                     print(f"{flags.error} Opss an error ); {colors.bright}{str(error)}{colors.reset}")
              finally:
                     print(f"{flags.finalization} See the result: {colors.bright}{path_result}{colors.reset}")

if __name__ == "__main__":
   print(f"Usage: {colors.bb}python extract_steg.py {colors.gb}path{colors.reset}")
   try:
      path = sys.argv[1].strip()
      extract_img(path)
   except Exception as error:
          print(f"{flags.error} Opss an error ); {colors.bright}{str(error)}{colors.reset}")
