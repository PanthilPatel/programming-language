#!/usr/bin/env python3
"""
Rock Paper Scissors Game
- Play against the computer.
- Best of 3 rounds (customizable).
"""

import random

def get_computer_choice():
    """Randomly returns rock, paper, or scissors."""
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    """Decides the winner of one round."""
    if user == computer:
        return "Draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "User"
    else:
        return "Computer"

def play_round():
    """Plays one round and returns the winner."""
    while True:
        user = input("Enter rock, paper, or scissors (or q to quit): ").strip().lower()
        if user in ["q", "quit", "exit"]:
            print("Goodbye!")
            exit(0)
        if user not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.")
            continue
        break

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")

    result = get_winner(user, computer)
    if result == "Draw":
        print("It's a draw!\n")
    elif result == "User":
        print("You win this round!\n")
    else:
        print("Computer wins this round!\n")
    return result

def play_game():
    """Main game loop."""
    print("Welcome to Rock Paper Scissors!")
    rounds = 3
    user_score = 0
    comp_score = 0

    for i in range(1, rounds + 1):
        print(f"--- Round {i} ---")
        result = play_round()
        if result == "User":
            user_score += 1
        elif result == "Computer":
            comp_score += 1

        print(f"Score: You {user_score} - {comp_score} Computer\n")

    print("=== Final Result ===")
    if user_score > comp_score:
        print("🎉 You win the game!")
    elif comp_score > user_score:
        print("😞 Computer wins the game!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
