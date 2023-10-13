grade = int(input("enter a grade: "))
level = int(input("insert the level: "))

if (level == 1):
    if (100 <= grade <= 71):
        print("distinction")
    elif (70 >= grade >= 61):
     print("merit")
    elif (60 >= grade >= 50):
      print("pass")
    else:
      print("fail")
    
if (level == 2):
    if (100 <= grade <= 66):
        print("distinction")
    elif (65 >= grade >= 51):
     print("merit")
    elif (50 >= grade > 40):
      print("pass")
    else:
      print("fail")