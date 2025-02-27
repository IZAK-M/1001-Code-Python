import os, time

rouge = "\033[91m"
vert = "\033[92m"
bleu = "\033[94m"
jaune = "\033[93m"
reset = "\033[0m" 

print("🏁🍕 IZAK's PIZZA 🍕🏁")

commande = []

try:
    fichier = open("commande.txt", "r")
    commande = eval(fichier.read())
    fichier.close()
except:
    print(f"{jaune}Vous êtes notre premier client. Merci 🙏🏻{reset}")
    print()

while True:
  print("Bonjour et bienvenue 👨🏽‍🍳")
  print()
  choix = input("Que voulez-vous faire ?\n1 : Commander\n2 : Voir les commandes en cours\n3 : Quitter\n> ")

  if choix == "1":
      while True:
          try:
              nombre_pizza = int(input("Combien de pizzas voulez-vous ? : "))
              break
          except:
              print("Erreur : la quantité doit être un nombre entier.")
      taille = input("Quelle taille S, M ou L ? : ").upper()
      nom = input("À quel nom ? : ")
      if taille == "S":
          prix = nombre_pizza * 5.99
      elif taille == "M":
          prix = nombre_pizza * 9.99
      else:
          prix = nombre_pizza * 14.99

      print(f"{jaune}Merci {nom} pour votre commande{reset}, \n{bleu}Pour vos pizzas, cela fera {prix} €{reset}")

      time.sleep(2)
      os.system("clear")

      ligne = [nombre_pizza, taille, nom, prix]
      commande.append(ligne)

      fichier = open("commande.txt", "w")
      fichier.write(str(commande))
      fichier.close()
  elif choix == "2":
      for ligne in commande:
          print(ligne)
  else:
    print("\033[32m","Merci de votre visite , Au revoir.", "\033[0m")
    time.sleep(2)
    os.system("clear")
    break