# create a list of students

students = [
    {'name':'Hermione','House':'Gryfindor','patronus':'Otter'},
    {'name':'Harry','House':'Gryfindor','patronus':'Stag'},
    {'name':'Ron','House':'Gryfindor','patronus':'Jack Russel terrir'},
    {'name':'Draco','House':'Slytherin','patronus':None}
]

# Create a header for the ur dictionary or list

print("Student Name\tStudents House\tStudents patronus")

# create a loop to get the value's from the dictionry keys'
for student in students:
    print(student['name'],student['House'],student['patronus'],sep =",\t")