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
         print(utilities_list)
         return utilities_list

def InstallUtilities(package_manager, utilities_list):
    match package_manager:
          case "portage":
               install = subprocess.run([""], check=True)
          case "pacman":
               install = subprocess.run([], check=True)
          case "apt":
               install = subprocess.run([], check=True)
          case _:
               print(f"Unknown or unsupported package manager {package_manager}")

if __name__ == "__main__":
   SudoAuthentication()
   read_utilities_list("utilities.txt")

"""
   args = sys.argv
   if args == 3:
      package_manager = args[1]
      utilities_file = args[2]
      try:
         #InstallUtilities(package_manager, utilities_file)
      except Exception as error:
             print(f"Se vira kkkk {str(error)}")
"""
'''
'''
