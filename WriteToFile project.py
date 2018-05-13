import random

def WriteToFile(nameOfFile,text):
    userFile=open(nameOfFile,"w")
    print("Hello, ", text, file=userFile) #wrote Hello to file using person's name
    userFile.close()

def main():
    nameIn= input("What is your name?")
    nameOfFileToWorkWith=input("What is your file name?")
    WriteToFile(nameOfFileToWorkWith,nameIn)
    print("ALL DONE...CHECK FILE")


def generateGPA():
    for i in range(50):
        gpa = str(random.randint(4,100))
        print(gpa)
    print("done")




majors = ["Biology", "Chemistry", "Mathematics", "Philosophy",
          "Dance", "History", "English","Computer Science", "Physics", "Undeclared"]

def randomMajors():
    majors = "Biology", "Chemistry", "Mathematics", "Philosophy",
    "Dance", "History", "English","Computer Science", "Physics", "Undeclared"
    for i in range (50):
        random.shuffle(majors)
        print (majors)


main()


