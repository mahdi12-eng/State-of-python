students = [
    {'name':'Mahdi','School':'Noor','field':'Developer'},
    {'name':'Mustafa','School':'Baba','field':'Dentist'},
    {'name':'Khalil','School':'Almito','field':'software engineering'},
    {'name':'Shafi','School':'Noor','field':None}
    ]

for student in students:
    print(student['name'],student['School'],student['field'],sep=', ')