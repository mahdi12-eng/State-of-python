def get_words(string):
    return "hi"

def main():
    counts ={}
    words = get_words("address.txt")


    for word in words:
        if word in counts:
            counts(word) +=1
        else:
            counts(word) = 1



