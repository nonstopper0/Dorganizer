import os
import shutil
from imported import *

global file

print('for the easiest method, please place the entire application folder within your downloads folder')

# move up the directory tree by one folder
os.chdir(os.path.dirname(os.getcwd()))

# a list of all the extensions in the folder
extensions = ['.JPG']

# read every file in the directory
i = 0
for file in os.listdir(os.getcwd()):
    i += 1
    new_file = os.path.splitext(file)
    extension_path = new_file[1].upper()
    # if the file isnt a folder
    if (extension_path != ''):
        if extension_path not in extensions:
            extensions.append(extension_path)
    print(f"{extension_path}\n{new_file}\n{i}\n\n")

print(f"extensions found: {extensions)")
