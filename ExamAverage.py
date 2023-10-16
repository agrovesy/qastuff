
math_mark = int(input("Enter the mark for Math: "))
while math_mark < 0 or math_mark > 100:
  print("Invalid mark. Please enter a mark between 0 and 100.")
  math_mark = int(input("Enter the mark for Math: "))
  
english_mark = int(input("Enter the mark for English: "))
while english_mark < 0 or english_mark > 100:
  print("Invalid mark. Please enter a mark between 0 and 100.")
  english_mark = int(input("Enter the mark for English: "))
  
ict_mark = int(input("Enter the mark for ICT: "))
while ict_mark < 0 or ict_mark > 100:
  print("Invalid mark. Please enter a mark between 0 and 100.")
  ict_mark = int(input("Enter the mark for ICT: "))

average_mark = int(math_mark + english_mark + ict_mark) / 3

if average_mark >= 65:
  result = "Pass"
else:
  result = "Fail"

print("Average mark:", average_mark)
print("Result:", result)