from pathlib import Path

# J'accede au dossier téléchargement 
telechargement = Path("/Users/izakmohamed/Downloads")


# Création de "Dossiers" et "Fichiers"

dossier = telechargement / "Dossiers"
fichier = telechargement / "Fichiers"

dossier.mkdir(exist_ok=True)
fichier.mkdir(exist_ok=True)

# lister tout les extentions de tout les fichier qui sont dans dossier et les mettre dans un set 

file_extensions = {f.suffix for f in telechargement.iterdir() if f.is_file}

# Pour chaque extensions de fichier , lui créer un dossier spécifique dans Fichiers
for e in file_extensions:
    extension = e.replace(".", "")

    extension_dir = fichier / extension
    extension_dir.mkdir(exist_ok=True)

# Deplacer chaque fichier dans son dossier correspondant 
for f in telechargement.iterdir():
    if f.is_file:
        extension = (f.suffix).replace(".", "")

        destination = Path(f"{fichier}/{extension}")

        chemin_final = destination / f.name

        # déplacer 
