def main():
    # create a game of moving boxes
    history = []

    while True:
        action = input("Action: ")
        
        # remove one item
        if action == "Undo":
            history.pop()
            print(history)

            # remove the whole list
        elif action == "Restart":
            history.clear()
            print(history)
        
        # add item 
        else:
            history.append(action)
            print(history)

main()