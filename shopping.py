# this progra will ask the user for their shopping items and 
# when done it will return the list to them

def main():
    completed_list = []
    shopping(completed_list)
    print(f"the food you wnat to buy are {completed_list}")



def shopping(shopping_list):
    while True:
        objects = input("What do you want to buy(enter 'done' to stop buying): ")
        if objects != 'done':
            shopping_list.append(objects)
        else:
            break
    return shopping_list
    
main()