courses = ['a', 'b', 'c', 'd']
courses2 = ['a', 'x', 'y', 'z']

# prints from 1st index to last but one-th
print(courses[1:-1])

# prints from 2nd index to last element in reverse order 
# i.e the first element in this case
print(courses[2::-1])

# insert courses2 list directly into courses list at index 1
courses.insert(1, courses2)
print(courses)

# append courses2 list directly to courses list
courses.append(courses2)
print(courses)

# modify the courses list by entering the contents of courses2 list
courses.extend(courses2)
print(courses)

print('---')

# convert courses2 list into a string with "--" between the elements
courses2_str = '='.join(courses2)
print(courses2_str)
print() # prints a new line

# convert string to a list based on a split value
list1 = courses2_str.split('=')
print(list1)

print('---')

# enumerate provides index and element of courses2 list
for ind, course in enumerate(courses2, start=2):
    print(ind, course)

print('---\nMutable\n---')
# lists are multable. i.e, change original list and the
# changes will be cascaded to the copied lists
list_1 = ['a', 'b', 'c', 'd']
list_2 = list_1

print(list_1)
print(list_2)

list_1[1] = 'x'

print(list_1)
print(list_2)
