import random

# The game's variables
score = 0
rolls = []

# Welcoming greetings for players
print("Welcome to DiceDom!")
print("In this game, you must roll the die until your total points add up to 50 points.")

# PLayer's starting point and addition of scores
while score < 50:
     input("Press Enter.")
     die = random.randint(1,6)
     score += die # Addition of scores
     rolls.append(die) # To update the player's scores

     print(f"You have earned {score} points!")
     print(f"You have earned a total of {score} points!")
    
# Congratulatory message for players after finishing the game
print("Game over")

# Ask the players if they would like to see the history of rolls
show_history = input("Do you want to see your history of rolls? (Yes/No): ").strip().lower()

# Display show history if players agree
if show_history == 'yes':
     print("History of your rolls:")
     for index, roll in enumerate(rolls, start=1):
          print(f"Roll {index}: {rolls}")

else:
     print("Thanks for playing!")
