import random, os, time
total_tentatives = 0

def jeu():
    tentatives = 0
    nombre = random.randint(1, 10000)
    while True:
        devine = int(input("Choisissez un nombre entre 1 et 10000 : "))
        if devine > nombre:
            print("C'est moins !")
            tentatives += 1
        elif devine < nombre:
            print("C'est plus !")
            tentatives += 1
        else:
            print("BIP BIP 🥳 C'est le juste prix ! 🥳")
            print(f"Vous avez trouvé en {tentatives} tentatives.")
            return tentatives

while True:
    menu = int(input("1 : Jouer au Juste Prix\n2 : Score total\n3 : Quitter\n> "))
    if menu == 1:
        os.system("clear")
        total_tentatives += jeu()
    elif menu == 2:
        print(f"Vous avez eu un total de {total_tentatives} tentatives.")
    else:
        print("Au revoir !")
        break
