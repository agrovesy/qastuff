shakes = { "Chocolate":[4], "Strawberry":[3], "Banana":[3], "Vanilla":[20]}
budget = int(input("what's your budget: "))
while True:
    choice = input("Enter choice(1, 2, 3, 4, ):")
    if choice == "Q":
        break
    value = shakes.get(choice, "Invalid choice") in shakes
    if value == "Invalid choice":
        print("Invalid choice")
        continue
    if value > budget:
        print("You can't afford that")
        continue
    budget - value
    print("You have £{} left".format(budget))