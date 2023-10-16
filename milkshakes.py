shakes = { "Chocolate":[4], "Strawberry":[3], "Banana":[3], "Vanilla":[20]}
budget = int(input("what's your budget: "))
while True:
    value = shakes.get(input("Enter choice(1, 2, 3, 4):"))
    print(value)

    if value in shakes:
        budget = (budget - value)
        print("budget left is {budget}")
  #  else:
  #      print("try picking an actual milkshake.")

#    break#

#else budget < shakes:
#    print("get out of here you bum")
    