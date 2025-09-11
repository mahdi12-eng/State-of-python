def main():
    # call the print_square function to execute the code
     print_square(3)

#create the function print_square
def print_square(area):
    for i in range(area):
        for j in range(area):
            print("#",end = "")
        print() 


# also possible to use the following method for the abbstraction

# create a function
def square(size):
    for _ in range(size):
        print("#"*size)
# !!! if you need you can easily call the function and execute the code    

main()
