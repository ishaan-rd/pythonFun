courses = {'Math', 'Science', 'English', 'History', 'Economics'}
art_courses = {'English', 'Design', 'History', 'Arts & Crafts'}

print(courses) # gives output in random order

# sets are optimised for 'membership' tests
print('English' in courses)

# intersection of two sets
print(courses.intersection(art_courses))

# difference of two sets
print(courses.difference(art_courses))

# union of two sets
print(courses.union(art_courses))
