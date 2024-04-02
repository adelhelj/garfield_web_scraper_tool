import os
import shutil

# Specify the source directory where the downloaded images are located
source_directory = '/Users/Username/Documents/Garfield/garfield_images' 
# Change to match your source directory

# Get a list of all files in the source directory
file_list = os.listdir(source_directory)

# Loop over each file
for file_name in file_list:
    # Split the file name to extract the year
    year = file_name.split('_')[0]

    # Create the destination directory for the year if it doesn't exist
    year_directory = os.path.join(source_directory, year)
    if not os.path.exists(year_directory):
        os.makedirs(year_directory)

    # Move the file to the destination directory
    source_path = os.path.join(source_directory, file_name)
    destination_path = os.path.join(year_directory, file_name)
    shutil.move(source_path, destination_path)

    print(f'Moved file: {file_name} to {year_directory}')
