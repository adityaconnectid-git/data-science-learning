# Day 08 - File Input and Output
# Topic: File Input and Output

# Example 1: Open and read the file
f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# Example 2: open and write in the file
st = "Hey, Rohan you are amazing"
f = open("file.txt", "w")
f.write(st)
f.close

# Example 3: Read line 
f = open("file.txt")
line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
f.close()

# Example 4: Read line using loop
f = open("file.txt")
line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()
f.close()

# Example 5: Read lines
f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close

# Example 6: Add at the end of the file
st = "Hey, Rohan you are so powerful"
f = open("file.txt", "a")
f.write(st)
f.close

# Example 7: Open the file by with statement 
with open("file.txt") as f:
    print(f.read())
# There is no need to close the file

# Example 8: Find twinkle is present in the contant or not
f = open("file.txt")
content = f.read()
if ("twinkle" in content):
    print("Yes , it present in this")
else:
    print("No , it is not present in this")
f.close()

# Example 9: The game() function in a program lets a user play a game and returns the score
#as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
#contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random
def game ():
    print("You are playing the game")
    score = random.randint(1,100)
    #fatch the high score
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"Your score : {score}")
    if (score>highscore):
        #write highscore in the file 
        with open("highscore.txt","w") as f :
            f.write(str(score))
    return score
game()

# Example 10: Write a program to generate multiplication tables from 2 to 20 and write it to the
#different files. Place these files in a folder for a 13 – year old.
def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} * {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt" , "w") as f:
        f.write(table)
for i in range (2,21):
    generateTable(i)

# Example 11: A file contains a word “Donkey” multiple times. You need to write a program
#which replace this word with ##### by updating the same file. 
word = "donkey"
with open("file.txt") as f :
    contant = f.read()
contantNew = contant.replace(word , "#####")
with open("file.txt" , "w") as f :
    f.write(contantNew)

# Example 12: Write a program to mine file and find out whether it contains ‘python’
with open("file.txt") as f:
    contant = f.read()
if ("python " in contant):
    print("Yes python is present ")
else:
    print("NO python is present")
with open("file.txt") as f:
    lines = f.readlines()

# Example 13: Write a program to find out the line number where python is present in previous example
with open("file.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines :
    if("python" in line ):
        print(f"Yes python is present in line {lineno} ")
        break
    lineno += 1
else:
    print("NO python is not present")

# Example 14: Write a program to make a copy of a text file “file.txt”
with open("file.txt") as f :
    contant = f.read()
with open("newcopy.txt" , "w") as f :
    f.write(contant)