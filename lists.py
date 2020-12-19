courses = ['a', 'b', 'c', 'd']
courses2 = ['x', 'y', 'z']

print(courses[1:-1])
print(courses[2::-1])

courses.insert(1, courses2)
print(courses)
courses.append(courses2)
print(courses)
courses.extend(courses2)
print(courses)

print('---')

courses2_str = '--'.join(courses2)
print(courses2_str)

print('---')

for ind, course in enumerate(courses2, start=2):
    print(ind, course)