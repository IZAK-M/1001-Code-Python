import random

list_choice = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_pick = input("-- Make your choice between -- \n rock 🪨 | paper 📄|scissors ✄ or Q to quit: ").lower()

    if user_pick == "q":
        break

    if user_pick not in list_choice:
        quit()

    computer_pick = list_choice[random.randrange(len(list_choice))]
    print(f"Computer chose : {computer_pick}.")

    if user_pick ==  computer_pick:
        print("equality")
    elif user_pick == "paper" and computer_pick == "rock":
        print("YOU WIN !")
        user_wins +=1
    elif user_pick == "rock" and computer_pick == "scissors":
        print("YOU WIN !")
        user_wins +=1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("YOU WIN !")
        user_wins +=1
    else:
        print("You lost !")
        computer_wins += 1


print(f"Final score : \nYou won {user_wins} times \nComputer won {computer_wins} times")

if user_wins == computer_wins:
    print("Egality 🤝")
elif user_wins < computer_wins:
    print("Computer win ! 🤖")
else:
    print("You Win 🥳 !")

print("GoodBye See you next time ! 👋")
