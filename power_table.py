# Ask the user for a number and then print a table of n, n square, and n cube

def power_table():
    
    # handle the possible errors
    while True:
        try:
            number =  int(input("enter a number: "))
            
            # design and set header alignment
            print(f"-"*20,"|")
            print(f"{'Number':^6}|{'Square':^6}|{'Cube':^7}|")
            
            for i in range(1,number+1):

                # set table body align
                print(f"{i:^6}|{i**2:^6}|{i**3:^7}|")
        
        # handle the error
        except ValueError:

            print("Required integer! please enter an integer")
        else:
            break

    print('The number successfully computed!')

power_table()