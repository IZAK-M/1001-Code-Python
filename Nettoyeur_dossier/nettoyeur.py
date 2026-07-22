from pathlib import Path

print("--🧹 Bienvenue dans ce Nettoyeur de dossier 🧹---")

# Accéder au dossier téléchargement
telechargement = Path(input("Écrivez le chemin du dossier : ")).expanduser()

if not telechargement.exists():
    print("❌ Le chemin indiqué n'existe pas.")
    exit()

# Création des dossiers "Dossiers" et "Fichiers"
dossier = telechargement / "Dossiers"
fichier = telechargement / "Fichiers"

dossier.mkdir(exist_ok=True)
fichier.mkdir(exist_ok=True)

# Lister toutes les extensions des fichiers
file_extensions = {f.suffix for f in telechargement.iterdir() if f.is_file()}

# Créer un dossier pour chaque extension
for ext in file_extensions:
    extension_name = ext.replace(".", "")
    extension_dir = fichier / extension_name
    extension_dir.mkdir(exist_ok=True)

# Déplacer chaque fichier dans son dossier correspondant
for f in telechargement.iterdir():
    if f.is_file():
        extension_name = f.suffix.replace(".", "")
        destination = fichier / extension_name
        chemin_final = destination / f.name

        # Gestion des collisions
        if chemin_final.exists():
            chemin_final = destination / f"copy_{f.name}"

        f.rename(chemin_final)

print("✅ Fichiers rangés avec succès")

# Déplacer les dossiers dans "Dossiers"
for d in telechargement.iterdir():
    if d.is_dir():
        # Ignorer les dossiers créés par le script
        if d.name in ("Dossiers", "Fichiers"):
            continue
        
        chemin_final = dossier / d.name

        # Gestion des collisions
        if chemin_final.exists():
            chemin_final = dossier / f"{d.name}_copy"

        d.rename(chemin_final)

print("✅ Dossiers rangés avec succès")
print("--- Programme terminé ---")
