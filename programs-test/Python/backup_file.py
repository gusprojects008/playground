import os
import shutil

def backup_process(path: str):
    file_expanded_path = os.path.expanduser(path)
    backup_file_path = file_expanded_path + ".old"
    os.makedirs(os.path.dirname(file_expanded_path), exist_ok=True)
    if os.path.exists(file_expanded_path):
       shutil.copy2(file_expanded_path, backup_file_path)
       print(f"Backup existing config: {file_expanded_path} -> {backup_file_path}")
    else:
        open(backup_file_path, "w").close()
        print(f"{file_expanded_path} not exist! created backup empty file in {backup_file_path}")
       
backup_process("./teste1/file.config")
