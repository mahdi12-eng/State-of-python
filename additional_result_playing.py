results =["Mario","Luigi","Princess","Yoshi","Koopa Troopa","Toad","Bowser","Donkey Kong Jr."]

# remove boswer from the list
results.remove("Bowser")

# add Boswer to the list
# results.append("Bowser")--->results =["Mario","Luigi","Princess","Yoshi","Koopa Troopa","Toad","Donkey Kong Jr.","Bowser"]

# use a new method to add in previous place
results.insert(0,"Bowser")  #--> replace with the Mario 

#  reverse the lsit for more better playing
results.reverse()

print(results)