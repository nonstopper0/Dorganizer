import os
import shutil

# move up the directory tree by one folder
os.chdir(os.path.dirname(os.getcwd()))

# list of extentions for sorting
videos = ['.MP4', '.MOV', '.WMV', '.FLV', '.AVCHD']
images = ['.JPEG', '.JPG', '.PNG', '.TIFF', '.BMP', '.RAW', '.ARW', '.NEF', '.WMF', '.TGA', '.JFIF', '.PSD', '.TIF', '.EPS']
compressed = ['.7Z', '.ZIP', '.ARJ', '.DEB', '.PKG', '.TAR.GZ', '.Z', '.RAR', '.RPM']
applications = ['.APP', '.EXE', '.MSI']
music = ['.MP3', '.WAV', '.WMA', '.M4A', '.AAC']
directories = ['Videos', 'Images', 'Music', 'Applications', 'Compressed', 'Files']
for direc in directories:
    try:
        os.mkdir(os.path.join(os.getcwd(), direc))
    except: 
        print('directories have already been created')



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
            directory = 'Videos'
        elif extension in images:
            directory = 'Images' 
        elif extension in compressed:
            directory = 'Compressed'
        elif extension in music:
            directory = 'Music'
        elif extension in applications:
            directory = 'Applications'

        # file extension matched one of the specified formats and is being categorized
        if directory:
            shutil.move(file_path, os.path.join(os.getcwd(), directory))

        # if file does not match with any categories listed
        if directory == False: 
            shutil.move(file_path, os.path.join(os.getcwd(), 'Files'))
            
        # keep a tab of the extensions
        if extension not in extensions:
            extensions.append(extension)

print(f"files moved: {i}\nextensions found: {extensions}")
