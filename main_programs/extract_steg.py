import subprocess

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
              try:
                 exif_data = subprocess.run(['exiftool', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=True)
                 info_img = subprocess.run(['binwalk', '-v', path], capture_output=True, text=True, check=True)
                 hex_content_img = subprocess.run(['xxd', path], capture_output=True, text=True, check=True)

                 file_result.write(f"Basic Data:\n{exif_data.stdout.decode('utf-8')}\n")
                 file_result.write(f"Info Image:\n{info_img.stdout}\n")

                 file_result.write(f"Hex content:\n{hex_content_img.stdout}\n")
                 file_result.write(f"Hex content:\n")

                 for char in hex_content_img.stdout:
                     if char.isalpha():
                         file_result.write(char)
                 file_result.write("\n")
                  
              except Exception as error:
                     print(f"{flags.error} Opss an error ); {colors.bright}{str(error)}{colors.bright}")
              finally:
                     print(f"{flags.finalization} See the result: {colors.bright}{path_result}{colors.reset}")
     

path = input("Type it path: ")
extract_img(path)
	
	
							
