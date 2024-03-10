import random

# Define a function to play the game
def play_game():
    global player_score
    # Define the valid choices
    choices = ["rock", "paper", "scissors"]
    # The computer makes a random choice
    computer_choice = random.choice(choices)
    # The user is prompted to make a choice
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # If the user's choice is not valid, print an error message and return
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    # Print the computer's choice
    print(f"Computer chose: {computer_choice}")
    # Print the user's choice
    print(f"You chose: {user_choice}")

    # If the user's choice is the same as the computer's, it's a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    # If the user's choice beats the computer's, the user wins
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        # Increase the player's score
        player_score += 1
    # Otherwise, the computer wins
    else:
        print("Computer wins!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    # If they do, call the function again
    if play_again == "yes":
        play_game()

# Initialize the player's score
player_score = 0
# Start the game
play_game()
# Print the player's final score
print(f"Your score: {player_score}")