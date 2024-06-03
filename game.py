import random

def get_user_choice():
    print("Enter your choice: Rock, Paper, or Scissors")
    user_choice = input().capitalize()
    while user_choice not in ['Rock', 'Paper', 'Scissors']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input().capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Scissors' and computer_choice == 'Paper') or
        (user_choice == 'Paper' and computer_choice == 'Rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Do you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()