grade = int(input("enter a grade: "))

if 100 <= grade <= 71:
    print("distinction")
elif 70 >= grade >= 61:
    print("merit")
elif 60 >= grade >= 50:
    print("pass")
else:
    print("fail")