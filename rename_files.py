# rename_files.py
# Usage: python rename_files.py <root_dir> <file_name> <new_name> [--recursive]

import os
import sys

def rename_files_and_dirs(root_dir: str, file_name: str, new_name: str, recursive: bool = False):
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            if dir == file_name:
                old_dir_path = os.path.join(root, dir)
                new_dir_path = os.path.join(root, new_name)
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed: {old_dir_path} to {new_dir_path}")
        for file in files:
            if file == file_name:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")
        if recursive:
            for dir in dirs:
                rename_files_and_dirs(os.path.join(root, dir), file_name, new_name, recursive)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python rename_files.py <root_dir> <file_name> <new_name> [--recursive]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    file_name = sys.argv[2]
    new_name = sys.argv[3]
    recursive = "--recursive" in sys.argv
    
    rename_files_and_dirs(root_dir, file_name, new_name, recursive)
