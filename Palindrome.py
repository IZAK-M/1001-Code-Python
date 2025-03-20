import os

# Couleurs (codes ANSI pour la console)
rouge = "\033[91m"
vert = "\033[92m"
jaune = "\033[93m"
reset = "\033[0m" 

# Fonction qui vérifie si le mot est un palindrome en utilisant la récursivité
def palindrome(mot):
  if len(mot) <= 1:  # Cas de base : un mot vide ou de longueur 1 est un palindrome
    return True
  if mot[0] != mot[-1]:  # Si les deux caractères aux extrémités ne correspondent pas
    return False
  return palindrome(mot[1:-1])  # Vérifie le mot sans les caractères des extrémités

# Boucle principale destinée à l'utilisateur
while True:
  print("🕵️‍♂️ DÉTECTEUR DE PALINDROMES 🕵️‍♀️")
  choix = input("1 : Tester un mot  2 : Quitter\n> ")
  os.system("clear")
  print("🕵️‍♂️ DÉTECTEUR DE PALINDROMES 🕵️‍♀️")
  if choix == "1":
    mot = input("Entrez un mot : ")
    if palindrome(mot):
      print(f"{vert}{mot} est un PALINDROME 👍{reset}")
    else:
      print(f"{rouge}{mot} n'est pas un PALINDROME 👎{reset}")
  elif choix == "2":
    print(f"{jaune}Au revoir 👋{reset}")
    break
  else:
    print(f"{rouge}Option invalide, veuillez réessayer !{reset}")
