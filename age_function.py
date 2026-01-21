# Task: create a function that get age and name as input
def info():
    
    # ask the user for their name
    name = input("please type your name: ").title()
   
    
    # handle the possible error 

    while True:

        try:
            
            age = int(input(f"Dear {name} please enter your age: ") )   
            
            # check the conditon for being elder or no
            if age > 0 :
                
                if age > 17:
                    print(f"Dear {name} you are elder. ")
                    break
                
                else:
                    print(f"Dear {name} you are under age. ")
                    break
            
            else:
                print(" plase enter a valid age! ") 
                continue
        
        # check the exception
        except ValueError:
            
            print(f"Dear {name}! enter age, expected integer, found string. ")


# Call the function for to display the output
info()