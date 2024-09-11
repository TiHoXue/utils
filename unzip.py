# unzip.py
# Usage: python unzip.py <root_dir> [--recursive]

import os
import zipfile

def unzip_files(root_dir, recursive=False):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                print(f"Unzipped: {zip_path}")
        if recursive:
            for dir in dirs:
                unzip_files(os.path.join(root, dir), recursive)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python unzip.py <root_dir> [--recursive]")
        sys.exit(1)
    root_dir = sys.argv[1]
    recursive = "--recursive" in sys.argv
    unzip_files(root_dir, recursive)