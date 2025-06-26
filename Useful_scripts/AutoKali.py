# python 3.10+
import sys
import os
import subprocess

def PrivilegiesVerify():
    if os.getuid()

def InstallUtilities(package_manager, utilities_list):
    match package_manager:
          case "portage":
               install = subprocess.run([], check=True)
          case "pacman":
               install = subprocess.run([], check=True)
          case "apt":
               install = subprocess.run([], check=True)
          case _:
               print(f"Unknown or unsupported package manager {package_manager}")
            
if __name__ == "__main__":
   args = sys.argv
   if args == 3:
      package_manager = args[1]
      utilities_list = args[2]
      try:
         InstallUtilities(package_manager, utilities_list)
      except Exception as error:
             print(f"Se vira kkkk {str(error)}")
   else:
       print("Usage: python AutoKali.py <package manager name> <utilities list path>")
