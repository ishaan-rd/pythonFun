# tuples are not mutable
tuple_1 = ('a', 'b', 'c', 'd')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[1] = 'x' # throws error because can't change

print(tuple_1)
print(tuple_2)