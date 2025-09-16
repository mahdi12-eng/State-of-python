def main():
    # create dictionary 
    spacecraft = {"name":"James Web Space Telescope","distance":34}

    # update the dictionary with you info
    spacecraft.update({"name":"Siwa","country":"Afghanistan"})

    
    # print the result
    print(create_report(spacecraft))

# create function to use dictionary 
def create_report(spacecraft):

    # use format string for result & design your favorite output
    return f"""
    =============================================== Report ==================================
     |   \   |======/||\   |===> Name: {spacecraft.get("name","unknown")}😍                  
     |    \  |=====/ || \  |===> Distance: {spacecraft.get("distance","unknown")} AU 😲                   
     |     \ |====/  ||  \ |===> Address: {spacecraft.get("country","Ooops")}🤭              
     |      \|===/   ||   \|===> Citizen:{spacecraft.get("citizenship","HEY YOU")}😡         
    =========================================================================================
    """

# call the main function for the code execution
main()