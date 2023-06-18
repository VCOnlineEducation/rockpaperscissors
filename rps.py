import random
from IPython.display import clear_output

rock = '''
    _______
---'   ____)
      (_____)
  💎  (_____)
       (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
   🧻    _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
    ✂  __________)
      (____)
---.__(___)
'''

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        clear_output()  # Clear the output
        print("Let's play Rock, Paper, Scissors!")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("You chose:")
        print(eval(user_choice))  # Using eval() to print the corresponding ASCII representation

        print("Computer chose:")
        print(eval(computer_choice))

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()
