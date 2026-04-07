import os
import time

folder = input("Enter folder path: ")

if not os.path.isdir(folder):
    print("Invalid folder path")
else:
    previous_files = set(os.listdir(folder))

    print("\nWatching for changes...\n")

    while True:
        time.sleep(2)
        current_files = set(os.listdir(folder))

        added = current_files - previous_files
        removed = previous_files - current_files

        for file in added:
            print(f"File added: {file}")

        for file in removed:
            print(f"File removed: {file}")

        previous_files = current_files
