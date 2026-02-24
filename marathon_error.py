def main():
    minute = 0
    while True:
        try:
            minute = float(input("enter minute: "))
            break
        except ValueError:
            print("invalid minute!")
    pace = get_pace( 26.2,minute)
    print(f"you need to run each mile in {round(pace,2)} minutes.")


def get_pace(miles,minutes):
    while True:
        if not minutes > 0:
            raise ValueError("Invalid value for minute")
        return miles/minutes
main()