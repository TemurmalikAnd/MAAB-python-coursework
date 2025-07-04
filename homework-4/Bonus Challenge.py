from random import choice

def main():
    """Main game function for Rock Paper Scissors."""
    options = ["rock", "scissors", "paper"]
    computer_score = 0
    player_score = 0
    
    print("Welcome to Rock Paper Scissors!")
    print("First to 5 wins!")
    
    while computer_score < 5 and player_score < 5:
        computer_choice = choice(options)
        player_choice = input("Choose one (rock, paper, scissors): ").lower().strip()
        
        # Validate player input
        if player_choice not in options:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            print("It's a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You won this round!")
            player_score += 1
        else:
            print("Computer won this round!")
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        print("-" * 40)
    
    # Final results
    if player_score == 5:
        print("Congratulations! You won the game!")
    else:
        print("You lost the game!")
    
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()