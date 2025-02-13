import random
import os

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Banque de mots d'animaux
mots = ('fourmi babouin blaireau chauve-souris ours castor chameau chat '
         'palourde cobra couguar coyote corbeau cerf chien âne canard aigle '
         'furet renard grenouille chèvre oie faucon lion lézard lama '
         'taupe singe élan souris mule triton loutre hibou panda perroquet '
         'pigeon python lapin bélier rat corbeau rhinocéros saumon phoque '
         'requin mouton putois paresseux serpent araignée cigogne cygne '
         'tigre crapaud truite dinde tortue belette baleine loup wombat zèbre').split()

# Sélection du mot à deviner de manière aléatoire :
mot_aleatoire = random.choice(mots)

# Début du jeu

lettre_choisie = []
tentatives = 6

while True:
  
  print('\n🌟PENDU🌟\n')
  choix = input('Choisis une lettre : ').lower()
  os.system('clear')
  
  if choix in lettre_choisie:
    print('Tu as déjà utilisé cette lettre ')
    continue
  lettre_choisie.append(choix)
  if choix in mot_aleatoire:
    print("Correct ! ✅")
  else:
    print("Mauvaise réponse ⛔️")
    tentatives -= 1
    print(hangmanpics[abs(6-tentatives)])

  print()
  print(f"Il vous reste {tentatives} tentatives ")
  print()

  toutes_lettres = True
  for lettre in mot_aleatoire:
    if lettre in lettre_choisie:
      print(lettre, end="")
    else:
      print("_", end="")
      toutes_lettres = False
      
  print()
  if toutes_lettres:
    print(f"🥳 Vous avez gagné avec {tentatives} tentatives restantes ! 🎖️")
    break
  elif tentatives <= 0:
    print('Vous êtes mort ☠️ GAME OVER ☠️')
    print(f'Le mot correct était {mot_aleatoire}')
    break
