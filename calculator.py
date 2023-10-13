
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
choice = input("Enter choice(1, 2, 3, 4, 5):")

if choice == '1':
    print(number1 + number2)
elif choice == '2':
    print(number1 - number2)
elif choice == '3':
    print(number1 * number2 )
elif choice == '4':
    if number2 == 0:
     print("Error! denominator cannot be zero")
elif choice == '5':
     print(number1 ** number2)
else:
        print(number1 /  number2 )
