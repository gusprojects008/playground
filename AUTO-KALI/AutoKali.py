# python 3.10+
import sys
import os
import subprocess
import getpass

def PrivilegiesVerify() -> bool:
    return os.getuid() == 0

def SudoAuthentication():
    if not PrivilegiesVerify():
       print("\nThis program requires administrator privilegies!\n")
       try:
          subprocess.run(["sudo", sys.executable] + sys.argv, check=True)
          print()
          sys.exit(0)
       except subprocess.CalledProcessError as error:
              print(f"\nSubprocess or authentication Error );\n{str(error)}")
              sys.exit(1)

def read_utilities_list(utilities_file):
    with open(utilities_file, "rt") as file:
         utilities_list = [line.strip() for line in file.readlines() if line.strip()]
         return utilities_list

def InstallUtilities(package_manager, utilities_list):
    utilities = read_utilities_list(utilities_list)

    match package_manager:
          case "pacman":
                try:
                   install = subprocess.run(["pacman", "--noconfirm", "-S"] + utilities, check=True)
                except Exception as error:
                       print(str(error))
          case "apt":
               try:
                  install = subprocess.run(["apt", "install", "-y"] + utilities, check=True)
               except Exception as error:
                      print(str(error))
          case _:
               print(f"Unknown or unsupported package manager {package_manager}")

def KaliTheme():
    

if __name__ == "__main__":
   usage = "usage: AutoKali.py --install <package manager name> utilities.txt"

   SudoAuthentication()
   
   args = sys.argv

   try:
      if args[1] == "--install":
         InstallUtilities(args[2], args[3])
      elif args[1] == "--kalitheme":
           print("Getting Kali Linux images...")
      else:
          print(f"Unknow arguments: {args}")
   except Exception as error:
          print(f"\nError! {usage}\n{error}")
