import os
import shutil
import json

def backup_process(path: str):
    file_expanded_path = os.path.expanduser(path)
    print(f"File expanded path: {file_expanded_path}")
    backup_file_path = file_expanded_path + ".old"
    os.makedirs(os.path.dirname(file_expanded_path), exist_ok=True)
    if os.path.exists(file_expanded_path):
       shutil.copy2(file_expanded_path, backup_file_path)
       print(f"Backup existing config: {file_expanded_path} -> {backup_file_path}")
    else:
       # open(backup_file_path, "w").close()
        open(file_expanded_path, "w").close()
        print(f"{file_expanded_path} not exist! created empty file in {file_expanded_path}")

with open("./packages.json", "r", encoding="utf-8") as file:
     json_data = json.load(file).get("System packages", {})

     for pkg, pkg_cfg in json_data.items():
         if isinstance(pkg_cfg, list):
            print(pkg_cfg)

#backup_process("./teste1/file.config")
