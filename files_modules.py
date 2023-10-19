#import math

#number = 10

#answer = math.sqrt(number)

#print(answer)


#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)


#for i in range(5):
#    print(random_pi())
    
    
#from math import pi, ceil, floor
#from random import randint

#def random_pi():
#    return floor(randint(1,6))

#for i in range(1,10):
#    print(random_pi())



#file = open("filename.txt", "mode") # r = readonly    w = write  r+ = read and write   a = append

#file.close()

#file = open("filename.txt", "r")
#file.read()
#print(file.readline())

#file.seek(0)
#print(file.readline())

#file.seek(20)
#print(file.readline())

#file.close()

#lines = file.readlines()

#print(lines)

#file.close()




#file = open("filename.txt", "w")

#for n in range(1, 11):
#    newline = "this is line" + " " + str(n) + "\n"
#    file.write(newline)
#    
#file.close()    

file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline
        
file = open("filename.txt", "w")

file.write(outfile)

file.close()
        
print(outfile)    
    
    


