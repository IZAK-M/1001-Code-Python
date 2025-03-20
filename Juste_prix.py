import random, os, time
total_tentatives = 0

# Fonction principale du jeu
def jeu():
    tentatives = 0
    nombre = random.randint(1, 10000)  # Génère un nombre aléatoire entre 1 et 10000
    while True:
        try:
            devine = int(input("Entrez un nombre entre 1 et 10000 : "))
            if devine > nombre:
                print("C'est moins !")  # Indique que le nombre choisi est trop grand
                tentatives += 1
            elif devine < nombre:
                print("C'est plus !")  # Indique que le nombre choisi est trop petit
                tentatives += 1
            else:
                print("BIP BIP 🥳 C'est le juste prix ! 🥳")  # L'utilisateur a trouvé le bon nombre
                print(f"Vous avez trouvé en {tentatives} tentatives.")
                return tentatives
        except ValueError:
            print("⛔ Erreur : Veuillez entrer un nombre valide.")  # Gestion des entrées non numériques

# Boucle principale pour le menu du jeu
while True:
    menu = int(input("1 : Jouer au Juste Prix\n2 : Voir le score total\n3 : Quitter\n> "))
    if menu == 1:
        os.system("clear")
        total_tentatives += jeu()  # Ajoute les tentatives de la partie au total
    elif menu == 2:
        print(f"Vous avez un total de {total_tentatives} tentatives.")  # Affiche le score total
    elif menu == 3:
        print("Au revoir !")  # Quitte le jeu
        break
    else:
        print("Option invalide, veuillez réessayer.")  # Message d'erreur en cas de saisie incorrecte
