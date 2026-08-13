from math_utils import add, subtract, multiply, divide

a = int(input("Define number a: "))
b = int(input("Define number b: "))

print(add(a,b))

print(subtract(a,b))

print(multiply(a,b))

division = divide(a,b)

if division is not None:
    print(division)
else:
    print("Division by 0 is not possible.")