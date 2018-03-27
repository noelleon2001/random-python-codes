# Programmer: Leon
import random
student=["Cici","James","Jonathan","Leon", "Matthew","Randy","Umar", "Zhi Yang"]
for people in student:
    print(people)
turn=1
while turn==1:
    input("Press ENTER pick a name randomly")
    name=student[random.randint(0,7)]
    print (name)