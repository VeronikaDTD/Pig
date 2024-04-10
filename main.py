import random


#Create a roll function that random rolls number between 1 - 6.
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)


#Create an input to find out how many players playing in digit.

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be Between 2 - 4 players. ")
    else:
        print("Invalid, Try again")

#Create a score variable that take in the value of the roll to player score.
max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:

    for player_idx in range(players):
        print("Player number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", players_score[player_idx], "\n")
        current_score = 0

        while True:

            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                value = roll()
                break
            value = roll()
            if value == 1:
                print("You roll a 1! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is ", current_score)

            players_score[player_idx] += current_score
            print("Your total score is: ", players_score[player_idx])

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print("Player number", winning_idx + 1, "is the winner with the score of:", max_score)