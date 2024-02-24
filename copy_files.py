import os
import shutil
import sys

def copy_files(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            copy_files(item_path, dest_dir)
        else:
            file_ext = os.path.splitext(item)[1][1:]
            dest_path = os.path.join(dest_dir, file_ext, item)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(item_path, dest_path)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 copy_files.py <source_directory> [destination_directory]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    try:
        copy_files(src_dir, dest_dir)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()