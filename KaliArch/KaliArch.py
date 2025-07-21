# python 3.13

import sys
import os
import subprocess
import getpass
import typing
import json

def PrivilegiesVerify() -> bool:
    return os.getuid() == 0 # return false if os.getuid() not equal to 0

def SudoAuthentication():
    if not PrivilegiesVerify():
       print("\nThis program requires administrator privilegies!\n")
       try:
          #subprocess.run(["sudo", "-k", sys.executable] + sys.argv, check=True)
          subprocess.run(["sudo", sys.executable] + sys.argv, check=True)
          sys.exit(0)
       except subprocess.CalledProcessError as error:
              print(f"\nSubprocess or authentication Error );")
              sys.exit(1)

def read_utilities_list(utilities_list_path: str) -> list[str]:
    with open(utilities_list_path, "r", encoding="utf-8") as file:
         return [line.strip() for line in file.readlines() if line.strip()]

def InstallUtilities(package_manager: str, utilities_list_path: str):
    utilities: list[str] = read_utilities_list(utilities_list_path)
    match package_manager:
          case "pacman":
               try:
                  subprocess.run(["pacman", "--noconfirm", "-S"] + utilities, check=True)
                  print(f"Installed: {', '.join(utilities)}")
               except subprocess.CalledProcessError as error:
                      print(f"Error installing with pacman: {error}")
          case other:
               print(f"Package manager '{other}' not supported for installation.")

def UninstallUtilities(package_manager: str, utilities_list_path: str):
    utilities = read_utilities_list(utilities_list_path)
    match package_manager:
          case "pacman":
               try:
                  subprocess.run(["pacman", "--noconfirm", "-Rns"] + utilities, check=True)
                  print(f"Uninstalled: {', '.join(utilities)}")
               except subprocess.CalledProcessError as error:
                      print(f"Error uninstalling with pacman: {error}")
          case other:
               print(f"Package manager {other} not supported for uninstallation.")

def InstallKaliTheme(package_manager: str, sec: int, mode: str, wallpapers_path: str):
    # backup

    with open("./kaliarch-themes/packages.json") as file:
         packages = json.load(file)
         packages_list = packages.keys()
         packages_config_paths = packages.values()

         

    # sec cannot be less then 1

    print("Installing Kali theme...") 
    pass

def UninstallKaliTheme(package_manager):
    print("Uninstalling Kali theme...") 
    pass

if __name__ == "__main__":
   usage = (
     "Usage:\n"
     "  --install-utilities <package manager> <utilities.txt>                            Install utilities\n"
     "  --uninstall-utilities <package manager> <utilities.txt>                          Uninstall utilities\n"
     "  --kalitheme-default <package manager>                                            Apply Kali theme default\n"
     "  --kalitheme-custom <package manager> --dynamic-background <sec> (<mode>) <DIR>   Dynamic wallpaper\n"
     "                                                                                   modes: --randomize, --ordered\n"
     "  --uninstall-kalitheme <package manager>                                          Remove Kali theme\n"
     "See how it works and what will be modified at: https://is.gd/z1VHiI"
   )

   args = sys.argv

   if len(args) < 2:
      print(usage)
      sys.exit(1)

   SudoAuthentication()

   rest = args[1:] # return the list of remaining arguments

   try:
      match rest:
            case ["--install-utilities", package_manager, utilities_list_path]:
                 InstallUtilities(package_manager, utilities_list_path)
            case ["--uninstall-utilities", package_manager, utilities_list_path]:
                 UninstallUtilities(package_manager, utilities_list_path)
            case ["--kalitheme-default", package_manager]:
                 InstallKaliTheme(package_manager, 300, "default", "~/wallpapers")
            case ["--kalitheme-custom", package_manager, "--dynamic-background", sec, mode, wallpapers_path]:
                 InstallKaliTheme(package_manager, sec, mode, wallpapers_path)
            case ["--uninstall-kalitheme", package_manager]:
                 UninstallKaliTheme(package_manager)
            case ["test"]:
                 InstallKaliTheme("pacman", 0, "default", "~/wallpapers")
            case _:
                print(f"Unknown arguments: {args[1:]}")
                print(usage, "\n")
      sys.exit(0)
   except Exception as error:
          print(f"Missing arguments or error );\n{str(error)}\n")
          print(usage)
          sys.exit(1)
