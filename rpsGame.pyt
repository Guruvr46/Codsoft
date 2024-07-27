import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if choice in ['rock', 'paper' , 'scissors']:
            return choice
        print("Invalid choice. Please try again. ")
        
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! "
    
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper' ) or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    
    else:
        return "Computer wins!"
    
    
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n----Rock-Paper-Scissors Game ----")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice : {computer_choice}")
        
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
            
        print(f"\nScore -You: {user_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
        
if __name__ == "__main__":
    play_game()