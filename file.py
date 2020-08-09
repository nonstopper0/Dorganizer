import os
import shutil

print('for the easiest method, please place the entire application folder within your downloads folder')

# move up the directory tree by one folder
os.chdir(os.path.dirname(os.getcwd()))

# list of extentions for sorting
videos = ['.MP4', '.MOV', '.WMV', '.FLV', '.AVCHD']
images = ['.JPEG', '.JPG', '.PNG', '.TIFF', '.BMP', '.RAW', '.ARW', '.NEF', '.WMF', '.TGA', '.JFIF', '.PSD', '.TIF', '.EPS']
compressed = ['.7Z', '.ARJ', '.DEB', '.PKG', '.TAR.GZ', '.Z', '.RAR', '.RPM']
os.mkdir(os.path.join(os.getcwd(), 'videos'))
os.mkdir(os.path.join(os.getcwd(), 'images'))
os.mkdir(os.path.join(os.getcwd(), 'compressed'))


# a list of all the extensions in the folder, keeps track of what directories have been made
extensions = []

# read every file in the directory
i = 0
for file in os.listdir(os.getcwd()):
    i += 1
    new_file = os.path.splitext(file)
    extension = new_file[1].upper()
    file_path = os.path.join(os.getcwd(), file)

    # if the file isnt a folder
    if (extension != ''):  
        directory = False 
        if extension in videos:
            directory = 'videos'
        elif extension in images:
            directory = 'images' 
        elif extension in compressed:
            directory = 'compressed'

        if directory:
            shutil.move(file_path, os.path.join(os.getcwd(), directory))
            
        # if extension_path not in extensions:
        #     extensions.append(extension_path)
        #     os.mkdir(os.path.join(os.getcwd(), directory))

    print(f"{extension}\n{new_file}\n{i}\n\n")

print(f"files found: {i}\nextensions found: {extensions}")
