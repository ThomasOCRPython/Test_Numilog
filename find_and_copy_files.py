import os
import shutil 
import docx

from list_files import list_pdf

# path_disk = "C:/Users/Latitude/Desktop/test"
# listing = "C:/Users/Latitude/Desktop/test/test"
destination = "C:/Users/Latitude/Desktop/test/destination"


def find_and_copy_files(path_disk, listing=list_pdf, path_destination=destination):
    create_folder(path_destination)
    listing_pdf = path_list_file(listing)
    for root, directories, files in os.walk(path_disk, topdown=False):
        list_file = [os.path.join(root, name) for name in files]
        for i in listing_pdf:
            for j in list_file:
                if i == j[-17:]:
                    file = j[-17:]
                    fullpath = j
                    if most_recent_file(file, fullpath, path_destination):
                        pass
                    else:
                        path = path_destination + "/" + "Mes100Fichiers"
                        shutil.copy(fullpath, path)


def most_recent_file(file, fullpath, path_destination):
    directory = path_destination + "/" + "Mes100Fichiers"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if f[-17:] == file:

            file_directory = os.stat(f)
            file_extern = os.stat(fullpath)
            if file_extern.st_atime <= file_directory.st_atime:
                return True


def create_folder(path_destination):
    directory = "Mes100Fichiers"

    parent_dir = path_destination

    path = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        os.mkdir(path)


def path_list_file(listing):
    directory = listing
    list_pdf = []
    for root, dirs, files in os.walk(directory):
        listpdf = [os.path.join(root, filename) for filename in files]
        for path_docx in listpdf:
            if path_docx[-5:] == ".docx":
                pathdocx = path_docx
                doc = docx.Document(pathdocx)
                result = [p.text for p in doc.paragraphs]
                for file in result:
                    if file[-4:] == ".PDF" and len(file) == 17:
                        list_pdf.append(file)
    return list_pdf


# path_list_file(listing)
# find_and_copy_files(path_disk, listing, path_destination)
# most_recent_file()
