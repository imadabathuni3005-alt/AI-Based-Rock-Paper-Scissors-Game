import random

# ==========================================
#     AI ROCK, PAPER, SCISSORS GAME
# ==========================================

print("=" * 50)
print("      AI ROCK, PAPER, SCISSORS GAME")
print("=" * 50)

moves = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
draws = 0

# Store player's move history
history = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

print("\nType Rock, Paper, or Scissors")
print("Type 'quit' to Exit\n")

while True:

    player = input("Your Move : ").lower()

    if player == "quit":
        break

    if player not in moves:
        print("Invalid Move! Try Again.\n")
        continue

    # Save player history
    history[player] += 1

    # AI Prediction
    predicted = max(history, key=history.get)

    # Computer chooses the winning move
    if predicted == "rock":
        computer = "paper"
    elif predicted == "paper":
        computer = "scissors"
    else:
        computer = "rock"

    print(f"Computer : {computer}")

    # Decide Winner
    if player == computer:
        print("Result : Draw")
        draws += 1

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):

        print("Result : You Win!")
        player_score += 1

    else:
        print("Result : Computer Wins!")
        computer_score += 1

    # Display Score
    print("-" * 35)
    print(f"You       : {player_score}")
    print(f"Computer  : {computer_score}")
    print(f"Draws     : {draws}")
    print("-" * 35)

print("\n===================================")
print("           FINAL SCORE")
print("===================================")
print(f"You       : {player_score}")
print(f"Computer  : {computer_score}")
print(f"Draws     : {draws}")

if player_score > computer_score:
    print("\n🏆 Congratulations! You Won the Game.")
elif computer_score > player_score:
    print("\n🤖 AI Wins the Game!")
else:
    print("\n🤝 Game Draw!")

print("\nThanks for Playing!")