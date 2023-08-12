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

copy = input("\nDo you want to copy new files to backup directory? (y/n): ")

if copy.lower().strip() == "y":
    for item in new_files:
        source_path = os.path.join(orginal_directory, item)
        destination_path = os.path.join(backup_directory, item)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        shutil.copy2(source_path, destination_path)
        print(f"Copying [{item}] to [{backup_directory}]")
    print("\nFiles copied successfully.")
else:
    print("\nNo files were copied.")