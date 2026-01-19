# this progrsm refer some card to th user based on the difficulty of the game
# defining a main functoin
def main():

    # Ask the user for the difficulty level(case sensetive)
    difficulty = input("Difficult or Casual? ")


# How to recommend(conditional)

# cases for Difficult
    if difficulty == "Difficult":
        
    # Ask the user for the playing mode
        players = input("Multiplayer or Single-player? ")
        if players == "Multiplayer":
            recommend("pocker")
        elif players == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of player: ")
    
    # Cases for Casual
    elif difficulty == "Casual":
        
    # Ask the user for the playing mode
        players = input("Multiplayer or Single-player? ")
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of player: ")
    
    #  Case for et cetra
    else:
        print("Enter a valid difficulty: ")

# Defining a sub function called recommend to store the recommendation for the user
#  based on the condition

def recommend(game):
    print("you might like",game)


# call the main function to execute the program
main()