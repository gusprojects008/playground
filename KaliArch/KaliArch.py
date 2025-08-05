# python 3.13

import sys
import os
import subprocess
import getpass
import typing
import json
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
THEMES_DIR = os.path.join(SCRIPT_DIR, "themes")
PACKAGES_JSON = os.path.join(THEMES_DIR, "packages.json")
DEVNULL = subprocess.DEVNULL
KALITHEME_PACKAGES = os.path.join(SCRIPT_DIR, "kalitheme_packages.txt")

def PrivilegiesVerify() -> bool:
    return os.getuid() == 0

def SudoAuthentication():
    if not PrivilegiesVerify():
        print("\nThis program requires administrator privileges!\n")
        try:
            subprocess.run(["sudo", sys.executable] + sys.argv, check=True)
            sys.exit(0)
        except subprocess.CalledProcessError as error:
            print("\nSubprocess or authentication Error );")
            sys.exit(1)

def read_utilities_list(utilities_list_path: str) -> list[str]:
    with open(utilities_list_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def InstallUtilities(package_manager: str, utilities_list_path: str):
    utilities = read_utilities_list(utilities_list_path)
    match package_manager:
        case "pacman":
            try:
                subprocess.run(["pacman", "-S", "--noconfirm"] + utilities, check=True)
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
                subprocess.run(["pacman", "-Rns", "--noconfirm"] + utilities, check=True)
                print(f"Uninstalled: {', '.join(utilities)}")
            except subprocess.CalledProcessError as error:
                print(f"Error uninstalling with pacman: {error}")
        case other:
            print(f"Package manager {other} not supported for uninstallation.")

def expand_path(path: str) -> str:
    return os.path.expanduser(os.path.expandvars(path))

def file_backup(path: str):
    expanded_path = expand_path(path)
    backup_path = expanded_path + ".old"
    
    if os.path.exists(expanded_path):
       shutil.copy2(expanded_path, backup_path)
       print(f"Backup created: {expanded_path} -> {backup_path}")
    else:
        os.makedirs(os.path.dirname(expanded_path), exist_ok=True)
        with open(expanded_path, 'w') as file:
             file.write("# Placeholder created by KaliArch installer\n")
        shutil.copy2(expanded_path, backup_path)
        print(f"Created placeholder and backup for: {expanded_path}")

def config_copy(src: str, dest: str):
    full_src = os.path.join(THEMES_DIR, src)
    full_dest = expand_path(dest)
    
    try:
       os.makedirs(os.path.dirname(full_dest), exist_ok=True)
       if os.path.isdir(full_src):
          if os.path.exists(full_dest):
             shutil.rmtree(full_dest)
             shutil.copytree(full_src, full_dest)
             print(f"Copied directory: {src} -> {dest}")
        else:
            shutil.copy2(full_src, full_dest)
            print(f"Copied file: {src} -> {dest}")
    except Exception as error:
           print(f"Copy failed: {src} -> {dest}: {error}")

def restore_from_backup(path: str):
    expanded_path = expand_path(path)
    backup_path = expanded_path + ".old"
    expanded_path_bak = expanded_path + ".bak"
    
    if os.path.exists(backup_path):
       try:
          if os.path.exists(expanded_path):
             config_copy(expanded_path, expanded_path_bak)
             shutil.move(backup_path, expanded_path)
             print(f"Restored backup: {backup_path} -> {expanded_path} And created backup of {expanded_path} in {expanded_path_bak}")
        except Exception as error:
               print(f"Restore failed: {backup_path} -> {expanded_path}: {error}")
    else:
        print(f"No backup found for: {expanded_path}")

def InstallKalitheme(package_manager: str):
    print("Installing Kali theme...")
    
    try:
        with open(PACKAGES_JSON, "r", encoding="utf-8") as file:
             json_data = json.load(file)
    except Exception as error:
           print(f"Failed to load packages.json: {error}")
           return
    
    system_packages = json_data.get("System packages", {}).get("kalitheme", {})
    packages_configs = json_data.get("Packages config", {}).get("kalitheme", {})
    
    with open(KALITHEME_PACKAGES, "w", encoding="utf-8") as file:
         for pkg, pkg_cfg in system_packages.items():
             if isinstance(pkg_cfg, list):
                for path in pkg_cfg:
                    file_backup(path)
             
             if subprocess.run(["pacman", "-Q", pkg], stdout=DEVNULL, stderr=DEVNULL).returncode != 0:
                file.write(pkg + "\n")
    
    InstallUtilities(package_manager, KALITHEME_PACKAGES)
    
    for pkg, pkg_cfg in packages_configs.items():
        system_pkg_cfg = system_packages.get(pkg):

        src_paths = [pkg_cfg] if isinstance(pkg_cfg, str) else pkg_cfg
        dest_paths = [system_pkg_cfg] if isinstance(system_pkg_cfg, str) else system_pkg_cfg
    
        if len(src_paths) != len(dest_paths):
           print(f"Warning: Mismatch in config files for {pkg} - expected {len(dest_paths)} files, got {len(src_paths)}")
           continue
    
        for src, dest in zip(src_paths, dest_paths):
            config_copy(src, dest)
           
    print("KaliTheme installed successfully!")

def UninstallKalitheme(package_manager: str):
    print("Uninstalling Kali theme...")
    try:
        with open(PACKAGES_JSON, "r", encoding="utf-8") as file:
             data = json.load(file)
    except Exception as error:
           print(f"Failed to load packages.json: {error}")
           return
    
    system_packages = data.get("System packages", {}).get("kalitheme", {})
    packages_configs = json_data.get("Packages config", {}).get("kalitheme", {})
    
    for pkg, pkg_cfg in system_packages.items():
        if isinstance(pkg_cfg, list):
           for path in pkg_cfg:
               restore_from_backup(path)
        else:
            restore_from_backup(pkg_cfg)
    
    UninstallUtilities(package_manager, KALITHEME_PACKAGES)
    
    print("KaliTheme uninstalled successfully!")

def dynamic_background(sec: int, mode: str, walpaper_path: str):

if __name__ == "__main__":
    usage = (
        "Usage:\n"
        "  --install-utilities <package manager> <utilities.txt>      Install utilities\n"
        "  --uninstall-utilities <package manager> <utilities.txt>    Uninstall utilities\n"
        "  --kalitheme-default <package manager>                      Apply Kali theme\n"
        " --dynamic-background <sec> <mode> <DIR>                     Dynamic wallpaper\n"
        "                                                             modes: --randomize, --ordered\n"
        "  --uninstall-kalitheme <package manager>                    Remove Kali theme\n"
        "See documentation: https://is.gd/z1VHiI"
    )

    args = sys.argv

    if len(args) < 2:
        print(usage)
        sys.exit(1)

    SudoAuthentication()

    remaining_args = args[1:]

    try:
       match remaining_args:
             case ["--install-utilities", package_manager, utilities_list]:
                  InstallUtilities(package_manager, utilities_list)
             case ["--uninstall-utilities", package_manager, utilities_list]:
                  UninstallUtilities(package_manager, utilities_list)
             case ["--kalitheme-default", package_manager]:
                  InstallKalitheme(package_manager)
             case ["--dynamic-background", sec, mode, wallpapers_path]:
                  dynamic_background(int(sec), mode, walpaper_path)
             case ["--uninstall-kalitheme", package_manager]:
                  UninstallKalitheme(package_manager)
             case _:
                  print(f"Unknown arguments: {remaining_args}")
                  print(usage)
       sys.exit(0)
    except Exception as error:
           print(f"Error: {str(error)}")
           print(usage)
           sys.exit(1)
