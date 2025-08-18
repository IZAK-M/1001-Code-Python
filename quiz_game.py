import random

print("🎮 Bien venue dans ce quiz game 🎲")

# Récupération des informations du joueur
name = input("quel est votre nom : ")
age = int(input("quel age avez vous : "))

jouer = True
while jouer:
    if age >= 18: 
        print(f"Félicitation {name} vous êtes majeur vous pouvez jouer")
        user_number_choice = int(input("choissez un nombre entre 1 et 5 : "))
        random_number = random.randint(1, 5)
        if user_number_choice == random_number:
            print("Bravo vous avez gagnez 1.000.000 €")
            
            jouer = bool(input("True ou False"))
            if jouer == True:
                continue
            else:
                break
        else:
            print("Domage vous avez perdu")
            print(f'Le Bon nombre était : {random_number}')
            jouer = bool(input("True ou False"))
            if jouer:
                continue
            else:
                break
    else:
        print("Vous êtes mineur vous n'avez pas le droit de jouer")
        break
