def main():
    number = get_number()
    mewo(number)


def mewo(n):
    for _ in range(n):
        print("Meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n



main()