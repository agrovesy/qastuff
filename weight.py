

# Get the weight from the user.
weight = float(input("Enter a weight: "))
# Get the unit of measurement from the user.
unit = input("Enter the unit of measurement (kg or lbs): ")
# Convert the weight to the desired unit.
if unit.lower() == "kg":
  converted_weight = weight * 2.20462
  print(f"{weight} kg is equal to {converted_weight} lbs.")
elif unit.lower() == "lbs":
  converted_weight = weight / 2.20462
  print(f"{weight} lbs is equal to {converted_weight} kg.")
else:
  print("Invalid unit of measurement.")
  
 