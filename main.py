import os
import hashlib
from datetime import datetime

def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(65536)
                if not data:
                    break
                sha1.update(data)
    except Exception as e:
        print(f"Error calculating SHA-1 for file {file_path}: {e}")
        return None
    return sha1.hexdigest()

def get_file_info(directory, output_file, excluded_files):
    try:
        with open(output_file, 'w') as f:
            for foldername, subfolders, filenames in os.walk(directory):
                for filename in filenames:
                    if filename in excluded_files:
                        continue  

                    file_path = os.path.join(foldername, filename)
                    try:
                        file_size = os.path.getsize(file_path)
                        modification_time = os.path.getmtime(file_path)
                        modification_time_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
                        sha1_hash = calculate_sha1(file_path)

                        f.write(f"{filename}, {file_size} bytes, {modification_time_str}, {sha1_hash}\n")
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")
            print(f"Scanning complete. Information written to {output_file}.")
    except Exception as e:
        print(f"Error opening output file {output_file}: {e}")

if __name__ == "__main__":
    directory_to_scan = os.path.dirname(os.path.abspath(__file__))
    output_file = 'file_info.txt'

    excluded_files = ['main.py', output_file]

    print(f"Scanning directory: {directory_to_scan}")
    get_file_info(directory_to_scan, output_file, excluded_files)
