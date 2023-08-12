#iJ

import os
import shutil

orginal_directory = input("Original files directory: ") 
backup_directory = input("Previous backup directory: ")

current_files = []
for root, _, files in os.walk(orginal_directory):
    for file in files:
        file_path = os.path.relpath(os.path.join(root, file), orginal_directory)
        current_files.append(file_path)

previous_files = []
for root, _, files in os.walk(backup_directory):
    for file in files:
        file_path = os.path.relpath(os.path.join(root, file), backup_directory)
        previous_files.append(file_path)

new_files = [item for item in current_files if item not in previous_files]

print("\nNew files:")
for item in new_files:
    print(item)