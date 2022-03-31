
import os
import shutil
from pathlib import Path
from list_files import list_pdf



if not os.path.exists('Mes100Fichiers'):
    os.mkdir('Mes100Fichiers')

path = 'C:/Users/Latitude/Desktop/test'
for root, directories, files in os.walk(path, topdown=False):
    list_file = [os.path.join(root, name) for name in files]
    for i in list_pdf:
        for j in list_file:
            if(i==j[-17:]):
                print(j)
                fullpath = j
                print(fullpath,2222)
                # shutil.copy(fullpath, os.mkdir('Mes100Fichiers'))
                shutil.copy(fullpath, 'Mes100Fichiers')
                print(i)
                break
	








