import os
import shutil

print('for the easiest method, please place the entire application folder within your downloads folder')

# move up the directory tree by one folder
os.chdir(os.path.dirname(os.getcwd()))

# list of extentions for sorting
videos = ['.MP4', '.MOV', '.WMV', '.FLV', '.AVCHD']
images = ['.JPEG', '.JPG', '.PNG', '.TIFF', '.BMP', '.RAW', '.ARW', '.NEF', '.WMF', '.TGA', '.JFIF', '.PSD', '.TIF', '.EPS']
compressed = ['.7Z', '.ZIP', '.ARJ', '.DEB', '.PKG', '.TAR.GZ', '.Z', '.RAR', '.RPM']
applications = ['.APP', '.EXE', '.MSI']
music = ['.MP3', '.WAV', '.WMA', '.M4A', '.AAC']
os.mkdir(os.path.join(os.getcwd(), 'Videos'))
os.mkdir(os.path.join(os.getcwd(), 'Images'))
os.mkdir(os.path.join(os.getcwd(), 'Music'))
os.mkdir(os.path.join(os.getcwd(), 'Applications'))
os.mkdir(os.path.join(os.getcwd(), 'Compressed'))
os.mkdir(os.path.join(os.getcwd(), 'Files'))


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
            
        # if extension_path not in extensions:
        #     extensions.append(extension_path)
        #     os.mkdir(os.path.join(os.getcwd(), directory))
    
    elif (extension == ''):
        print('folder found', file)

print(f"files found: {i}\nextensions found: {extensions}")
