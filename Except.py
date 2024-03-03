import sys
x = int(input("x: "))
y = int(input("y: ")) # Corrected the character for 'y'
try:
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError:
    print("Error:dividion by zero input")
sys.exit(1)