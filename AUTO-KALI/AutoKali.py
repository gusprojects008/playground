# python 3.10+

import sys
import os
import subprocess
import getpass
import argparse

def PrivilegiesVerify() -> bool:
    return os.getuid() == 0

def SudoAuthentication():
    if PrivilegiesVerify() == False:
       print("This program requires administrator privilegies!\n")
#       sudo_password = getpass.getpass(f"Password Sudo of user {os.environ['LOGNAME']} ")
       try:
          subprocess.run(["sudo", "-S", "python", sys.argv[0]], text=True, check=True)
          sys.exit(0)
       except Exception as error:
              print(f"\nAuthentication failure );\n{str(error)}")
              sys.exit(1)

def read_utilities_list(utilities_file):
    with open(utilities_file, "rt") as file:
         utilities_list = [line.strip() for line in file.readlines() if line.strip]
         return utilities_list

def InstallUtilities(package_manager, utilities_list):
    match package_manager:
          utilities = read_utilities_list(utilities_list)
          case "pacman":
                try:
                   install = subprocess.run(["pacman", "--noconfirm"] + utilities, check=True)
                except Exception as error:
                       print(str(error))
          case "apt":
               try:
                  install = subprocess.run(["apt", "install", "yes"] + utilities, check=True)
               except Exception as error:
                      print(str(error))
          case _:
               print(f"Unknown or unsupported package manager {package_manager}")

if __name__ == "__main__":
   SudoAuthentication()
   parser = argparser.ArgumentParser(
     prog="Autokali.py",
     description="Automates the intallation of cybersecurity and pentest tools!",
     epilog="--help"
   )
   package_manager = args[1]
      utilities_file_path = args[2]
      try:
         InstallUtilities(package_manager, utilities_file_path)
      except Exception as error:
             print(f"aprende a usar primeiro kkkk\n{str(error)}\nUsage:\n")
