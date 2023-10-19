
file = open("teams.txt", "w")


team = ["derby", "forest", "man city", "bham", "liverpool", "everton"]

for t in team:
    newline = "this is a football team" + " " + t + "\n"
    file.write(newline)

file.close()

file = open("teams.txt", "r")
lines = file.readlines()
file.close()

lines[0] = "this is a new line"
file = open("teams.txt", "w")
for i in range(len(lines)):
    if i == len(lines)-1:
        file.write(lines[i])
    else:
        file.write(lines[i].strip() + "\n")

file.close()

file = open("teams.txt", "r")
for line in file:
    print(line.strip())
file.close()
