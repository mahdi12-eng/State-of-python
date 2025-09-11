# this progrsm refer some card to th user based on the difficulty of the game

# defining a main functoin
def main():

    # Ask the user for the difficulty level(case sensetive)
    difficulty = input("Difficult or Casual? ")

    # cases for Difficult
    if  not (difficulty == "Difficult" or difficulty == "Casual"):    # if this condition is true print and return will be executed
        print("Enter a valid Difficulty: ")
        return                                                       # this return will stop the rest of the program from the execution
    
    # Ask the user for the playing mode
    players = input("Multiplayer or Single-player? ")

    if not (players == "Multiplayer" or players == "Single-player"):   # if true then print and return will execute
        print("Enter a valid number of players")
        return                                                          # if return execute the rest of program will not run 
        
    # Check the condition based on difficulity  
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("pocker")

    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")

    # Cases for Casual
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    
    else:
        recommend("Clock")
    
# Defining a sub function called recommend to store the recommendation for the user
# based on the condition

def recommend(game):
    print("you might like",game)


# call the main function to execute the program
main()