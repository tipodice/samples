import os
import json

folder_path = "."  # Replace with the path to your folder

# Get a list of all files in the folder
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Create a dictionary with the file names
file_list = {"files": files}

# Write the dictionary to a JSON file
with open("file_list.json", "w") as json_file:
    json.dump(file_list, json_file, indent=4)

print("JSON file 'file_list.json' created with the list of files.")

