# create the dictionary for daily bee game
WORDS = {"PAIR":4,"HAIR":4,"CHAIR":5,"GRAPHIC":7}

# create the function main for the code tracemet
def main():
    # Display an starting message
    print("Welcome to spelling Bee!")
    print("Your letters' are A I P C R H G ")

     # check whether the user is correct or no 
    while len(WORDS) > 0:

        # display how many words need to guess
        print(f"{len(WORDS)} words left!")
        # get the user guess by input
        guess = input("Guess a word: ")

        # TODO: check if guess in dictionary
        # check if the user used the whole letters in one word or no
        if guess == 'GRAPHIC':

            # clear the dictionary if the word matched
            WORDS.clear()

            # display the result message            
            print("You've won!")


        # check whether user guess correctly or no
        if guess in WORDS.keys():

            # delete the guessed key and value from the dictionay
            points = WORDS.pop(guess)

            # print the appreciate message to the user
            print(f"Good Job! you scored {points} points")

            # display the final message
    print("That's the game!")

    
# call the main function for code execution
main()