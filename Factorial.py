number = int(input("Enter an number: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print("The factorial is", factorial)