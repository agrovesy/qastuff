import random

while True:
    def playround():
        num_of_rounds = 0
        user_wins = 0
        computer_wins = 0
        rock = "rock"
        paper = "paper"
        scissors = "scissors"
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        user_choice = input("please pick your weapon: ")
        
        print(f"you have selected: {user_choice}")
        print(f"the computer has selected: {computer_choice}")
    
        if computer_choice == user_choice:
            print("draw")
            num_of_rounds += 1
            
        elif computer_choice == rock and user_choice == paper or computer_choice == scissors and user_choice == rock or computer_choice == paper and user_choice == scissors:
            print("you win")
            user_wins += 1
            num_of_rounds += 1
            
        elif computer_choice == rock and user_choice == scissors or computer_choice == scissors and user_choice == paper or computer_choice == paper and user_choice == rock:
            print("you lose")
            computer_wins += 1
            num_of_rounds += 1

        print("you have won {} games, the computer has won {} games and you have played for a total of: {} games".format(user_wins, computer_wins, num_of_rounds))

        if user_choice == "quit":
            return False

     #   return True

   # num_of_rounds = 0
   # user_wins = 0
   # computer_wins = 0

    while playround():
        num_of_rounds = 0
        num_of_rounds += 1