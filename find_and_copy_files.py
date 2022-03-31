import os
import shutil
from list_files import list_pdf

# path='C:/Users/Latitude/Desktop/test'


def find_and_copy_files(path_disk):
    create_folder()
    for root, directories, files in os.walk(path_disk, topdown=False):
        list_file = [os.path.join(root, name) for name in files]
        for i in list_pdf:
            for j in list_file:
                if i == j[-17:]:
                    file = j[-17:]
                    fullpath = j
                    if most_recent_file(file, fullpath):
                        pass
                    else:
                        shutil.copy(fullpath, "Mes100Fichiers")


def most_recent_file(file, fullpath):
    directory = "Mes100Fichiers"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f[15:] == file:
            file_directory = os.stat(f)
            file_extern = os.stat(fullpath)
            if file_extern.st_atime < file_directory.st_atime:
                return True


def create_folder():
    if not os.path.exists("Mes100Fichiers"):
        os.mkdir("Mes100Fichiers")


# find_and_copy_files(path)
# most_recent_file()
