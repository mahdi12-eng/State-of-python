# create the function average for computing the average of numbers
def average():
    amount = number_amount()
   user_list = user_number()
    if user_number != number_amount():
        print("fatal! the numbers you entered does not match the amount you specified.")

     
    
   
def user_number(amount):

 # create an empty list of number
    number = []
        
    # get the numbers from the user using loop
    for i in range(amount):
        while True:
            try:
                num = int(input(f"enter number {i+1} : "))
                number.append(num)
                break
            except ValueError:
                print("Invalid number, try again! ")
    return number
    # check wether number length is equal to amount defined in number_amount function
  
    
    
    



# define function amount to get the     
def number_amount():
    # check wether user type  a valid amount or no
    while True:
            
            try:
                
                # Ask the user for amount of number
                amount = int(input("How many number's do you want to get average of: "))
                
                # check wether amount is bigger then or no
                if amount != 0:

                    if amount > 1:
                        break       # stop the continuation if input is valid

                    elif amount < 0:
                      print("amount can not be negative! ") 
                    else:

                        print("Can not compute average! ")
                
                else:
                    print("Can't accept zero as amount! ")
                
            
            # check the exception 

            except ValueError:
                 print("Error! required positive integer: ")
    
    return amount
    
average() 