# 🧹 Nettoyeur de dossier

Un petit script Python qui range automatiquement un dossier en triant son contenu :
- les **fichiers** sont classés par extension dans un sous-dossier `Fichiers`
- les **dossiers** existants sont déplacés dans un sous-dossier `Dossiers`

## ⚙️ Fonctionnement

1. Le script demande le chemin du dossier à nettoyer.
2. Il crée deux dossiers à la racine : `Dossiers` et `Fichiers`.
3. Chaque fichier est déplacé dans `Fichiers/<extension>/` (ex : `Fichiers/pdf/`, `Fichiers/jpg/`...).
4. Chaque dossier (autre que ceux créés par le script) est déplacé dans `Dossiers/`.
5. En cas de conflit de nom (fichier ou dossier déjà présent à destination), le script ajoute automatiquement un préfixe/suffixe (`copy_` ou `_copy`) pour éviter d'écraser un élément existant.

## ▶️ Utilisation

```bash
python nettoyeur.py
```

Le script demande ensuite le chemin du dossier à nettoyer, par exemple :

```
Écrivez le chemin du dossier : ~/Downloads
```

## ⚠️ Remarques

- Le script déplace réellement les fichiers/dossiers (aucune copie de sécurité n'est faite au préalable). Il est conseillé de tester sur un dossier peu sensible avant utilisation.
- Si le chemin indiqué n'existe pas, le script s'arrête avec un message d'erreur.
- Le script est idempotent : il peut être relancé plusieurs fois sur le même dossier sans tout casser (les dossiers `Dossiers` et `Fichiers` sont ignorés lors des passages suivants).
