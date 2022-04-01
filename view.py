from find_and_copy_files import find_and_copy_files


def ask_disk():
    disk = input("Entrez le chemin de votre disk : ")
    list = input(
        "Tapez '1' pour entrer le chemin de la liste à trouver, tapez '2' pour utiliser la liste par défaut"
    )
    while list not in ("1", "2"):
        list = input(
            "Tapez '1' pour entrer le chemin de la liste à trouver, tapez '2' pour utiliser la liste par défaut"
        )
    list_file = list_file_find(list)

    folder = input(
        "Tapez 1 pour choisir le chemin de destination, tapez 2 pour un chemin de destination par defaut"
    )
    while folder not in ("1", "2"):
        folder = input(
            "Tapez 1 pour choisir le chemin de destination, tapez 2 pour un chemin de destination par defaut"
        )
    destination = folder_destination(folder)

    find_and_copy_files(disk, list_file, destination)


def list_file_find(nb):
    if nb == "1":
        list_file = input("Entrez le chemin de la list à trouver : ")
        return list_file
    else:
        pass


def folder_destination(nbr):
    if nbr == "1":
        destination = input("Entrez le chemin de destination : ")
        return destination
    else:
        pass
