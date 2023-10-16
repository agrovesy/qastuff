for i in range(3):
    user_num = int(input("please pick a number: "))
    min_range = 1
    max_range = 100
    if user_num in range(min_range, max_range):
        print(user_num)
        break
    elif min_range < user_num > max_range:
        print("pick a number between 1 and 100") 
    else:
        print("stopping this now")
        break