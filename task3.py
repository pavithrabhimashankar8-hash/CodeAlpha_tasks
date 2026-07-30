import os
import shutil

# Source folder path
source_folder = "source_images"

# Destination folder path
destination_folder = "destination_images"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Counter
count = 0

print("========== JPG FILE MOVER ==========")

# Check source folder
if os.path.exists(source_folder):

    files = os.listdir(source_folder)

    if len(files) == 0:
        print("No files found in source folder.")

    else:
        for file in files:

            source_path = os.path.join(source_folder, file)

            if file.lower().endswith(".jpg"):

                destination_path = os.path.join(destination_folder, file)

                shutil.move(source_path, destination_path)

                print(file, "Moved Successfully")

                count += 1

        print("----------------------------------")
        print("Total JPG Files Moved:", count)

else:
    print("Source folder does not exist.")

print("Program Finished.") 