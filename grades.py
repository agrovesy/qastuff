import statistics

grades= "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grade_split = grades.split(',')

gradesint = list(map(int, grade_split))
minimum = min(gradesint)
maximum = max(gradesint)
length = len(gradesint)
average = sum(gradesint)
decimal = round(average / length, 2)
#print(decimal)

average_grade = round(statistics.mean(gradesint), 2)
mode_grade = statistics.median(gradesint)

#print(average_grade)
#print(mode_grade)

print("the max is {}, the min is {}, the average is {} and the median is {}".format(maximum, minimum, average_grade, mode_grade))