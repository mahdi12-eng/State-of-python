# play with list attributes
#  initialize the list
results = ["Mario","Luigi"]

# add item to the list
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# qdd list to the list
results.append(["Bowser","Donkey Kong Jr"])

#remove list from the list
results.remove(["Bowser","Donkey Kong Jr"])

# add collection of element to the lsit
results.extend(["Bowser","Donkey Kong Jr"])

# print the final result
print(results)