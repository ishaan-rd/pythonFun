courses = ['a', 'b', 'c', 'd']
courses2 = ['x', 'y', 'z']

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
courses2_str = '--'.join(courses2)
print(courses2_str)

print('---')

# enumerate provides index and element of courses2 list
for ind, course in enumerate(courses2, start=2):
    print(ind, course)