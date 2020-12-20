# naming this file "numbers.py" made it behave weirdly where in
# this file was being called when tuples.py threw an error
# so renamed it to "python_numbers.py" and that behavior stopped
# investigate why this was happening

num1 = 22 / 7
num2 = 22 // 7

print(num1)
print(num2)

print(round(-2.6))
print(round(5.676, 2))

num3 = '100'
num4 = '200'

print(num3 < num4)