import random

def suit(score_player, score_computer):
    option = ["scissors", "rock", "paper"]
    computer = random.choice(option)
    
    #Looping untuk validasi input
    while True:
        player = input("Choose rock / paper / scissors = ").lower()
        if player in option:
            break
        else:
            print("Input Invalid! Try Again!")
            
    print("Computer choose = ", computer)
    
    if player == computer:
        print("DRAW!")
    elif(player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        print("PLAYER WIN!")
        score_player += 1
    else:
        print("COMPUTER WIN!")
        score_computer += 1
        
    print(f"Score Player = {score_player} Score Computer = {score_computer}")
    print("-" * 40)
    
    return score_computer, score_player

#insialisasi score
score_player = 0
score_computer = 0

#Looping game 
while True:
    score_player, score_computer = suit(score_computer, score_player)
    
    repeat = input("Play Again? (yes/no) = ").lower()
    if repeat != "yes":
        print("Thank You for Playing!")
        break