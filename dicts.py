student = {'name': 'John Wick', 'age': 22, 'courses': ['Math', 'CompSci']}

print(student)
print(student['courses'][1])
# print(student['email']) # throws error

# adding/updating values
student['email'] = 'johnwick@email.com'


# using the get method
print(student.get('name'))
print(student.get('email', 'Entry Not Found'))


# updating multiple keys
student.update({'age': 23, 'courses': ['CompSci', 'Finanace', 'Marketing']})

print(student)


# deleting keys
del student['age']
email = student.pop('email')

print(student)
print(email)

# ---
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
print('------')

# looping through dicts
for index in student:
    print(index) # prints only the keys

print('------')
for key, value in student.items():
    print(f'{key}: {value}')