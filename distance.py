distance ={
    "voyager 1":163,
    "voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizations":58,
    "Pionner 11":44
}


def main():
    for distances in distance.values():
        print(f"{distances} AU is {convert(distances)}m")
        
        for names in distance.keys():
            print(f"{names} Au is {distances}")


def convert(au):
    return au * 149597870700
main()