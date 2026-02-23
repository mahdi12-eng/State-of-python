# Write a program that asks the user for a name. 
# If the name exists in any of the departments,
#  print the name of that department. If not found, print "Employee not found."
def main():
    start_report = department_employee()
    print(start_report)
    company = {
        "Engineering": ["Alice", "Bob", "Charlie"],
        "Marketing": ["David", "Eve"],
        "Sales": ["Frank", "Grace", "Henry"]
        }
    found = False
    name = input("enter name: ")
    for department, employee in company.items():
        if name in employee:
            print(f"{name} is from department of {department}")
            found = True
            break
    if not found:
            print(" employee not found")
    end_report =end()
    print(end_report)
def department_employee():
   return f"""
******************************** Department Employee Report ********************************
    """

def end():
    return f"""
******************************** End Report *****************************************
    """
main()