import os
import shutil

print('for the easiest method, please place the entire application folder within your downloads folder')

# move up the directory tree by one folder
os.chdir(os.path.dirname(os.getcwd()))

videos = ['.MP4', '.MOV', '.WMV', '.FLV', '.AVCHD']
images = ['.JPEG', '.JPG', '.PNG', '.TIFF', '.BMP', '.RAW', '.ARW', '.NEF', '.WMF', '.TGA', '.JFIF', '.PSD', '.TIF', '.EPS']
compressed = ['.7Z', '.ARJ', '.DEB', '.PKG', '.TAR.GZ', '.Z', '.RAR', '.RPM']

# a list of all the extensions in the folder, keeps track of what directories have been made
extensions = []

# read every file in the directory
i = 0
for file in os.listdir(os.getcwd()):
    i += 1
    new_file = os.path.splitext(file)
    extension_path = new_file[1].upper()

    # if the file isnt a folder
    if (extension_path != ''):
        directory = False
        if extension_path in videos:
            directory = 'videos'
        elif extension_path in images:
            directory = 'images' 
        elif extension_path in compressed:
            directory = 'compressed'
        elif extension_path in 
        if extension_path not in extensions:
            extensions.append(extension_path)
            os.mkdir(os.path.join(os.getcwd(), extension_path[1:]))

    print(f"{extension_path}\n{new_file}\n{i}\n\n")

print(f"files found: {i}\nextensions found: {extensions}")
