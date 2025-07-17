import random
# a rock paper scissor game
# RPS game function 
def RPS_game():
    print("Game starts now")
    tries = 3
    player_wins = 0
    computer_wins = 0
    while tries > 0:
        p_choice = input("Rock/Paper/Scissor?: ")
        p_choice = p_choice.title().strip()
        c_choice = random.choice(["Rock","Paper","Scissor"])
        if p_choice == c_choice:
            print(f"that's a tie, you both had {p_choice} and {c_choice}")
        elif p_choice == "Rock" and c_choice == "Paper":
            computer_wins += 1
            print("Computer wins by paper!!")
            tries -=1
        elif p_choice == "Rock" and c_choice == "Scissor":
            player_wins += 1
            print(f"you won by Rock, the computer had {c_choice}! ")
            tries -=1
        elif p_choice == "Paper" and c_choice == "Scissor":
            computer_wins += 1
            print(f"Computer won by {c_choice}")
            tries -=1
        elif p_choice == "Paper" and c_choice == "Rock":
            player_wins += 1
            print(f"You won by {p_choice}")
            tries -=1
        elif p_choice == "Scissor" and c_choice == "Rock":
            computer_wins += 1
            print(f"Computer won by {c_choice}")
            tries -=1
        elif p_choice == "Scissor" and c_choice == "Paper":
            player_wins += 1
            print(f"you won by {p_choice}")
            tries -=1
    if tries == 0:
        print("no tries left")
    else:
        print(f"the number of tries left are {tries}")
    print("game over, here are the results")
    
    if computer_wins > player_wins:
        print(f"the computer won by {computer_wins} and you lost by {player_wins}")
    else:
        print(f"Player won by {player_wins} and computer lost by {computer_wins}")
    ch = input("Do you want to play again?(Yes/No)\n ")
    if ch.lower() == "yes":
        RPS_game()
    else:
        print(f"Alright, byee!")

# take user input and greetings
def greeting():
 name = input("enter your name: ")
 play_choice = input(f"Hello!, {name} welcome to RPS game \nDo you want to begin the game(yes/no): ")
 if play_choice.lower() == "yes":
     RPS_game()
 else:
    print("Alright, Good bye!")
greeting()
