from find_and_copy_files import find_and_copy_files


def ask_disk():
    disk = input("Entrez le chemin de votre disk : ")
    find_and_copy_files(disk)
