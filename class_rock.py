import random

class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    def player_choice(self, choice):
        if choice.lower() not in self.choices:
            print("Invalid choice, please choose 'rock', 'paper', or 'scissors'")
            return False
        return True

    def computer_choice(self):
        return random.choice(self.choices)

    def play_round(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif self.rules[player_choice] == computer_choice:
            return "You win!"
        else:
            return "You lose."

    def play_game(self):
        player_wins = 0
        computer_wins = 0
        ties = 0

        while True:
            print("\nChoose your move: rock, paper, or scissors")
            player_choice = input("Enter 'q' to quit game: ")

            if player_choice.lower() == 'q':
                break

            if not self.player_choice(player_choice):
                continue

            computer_choice = self.computer_choice()
            print(f"Player chose {player_choice}, Computer chose {computer_choice}")

            round_result = self.play_round(player_choice, computer_choice)
            print(round_result)

            if round_result == "You win!":
                player_wins += 1
            elif round_result == "You lose.":
                computer_wins += 1
            else:
                ties += 1

            print(f"Score: Player {player_wins}, Computer {computer_wins}, Ties {ties}")

game = Game()
game.play_game()