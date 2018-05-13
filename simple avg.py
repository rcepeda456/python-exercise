# avg2.py
#   A simple program to average two exam acores
#   Iilustraes use of multiple input

def simpleAvg():
    print("This program computes the average of two exam scores,")


    score1, score2 = eval(input("Enter two scores seperated by a comma: "))
    average = (score1 + score2) / 2

    print("The average of the scores is:" , average)

####################Ch.2 programming exercise 2. #########################################
def avg3numa():
    print("This program computes the average of three exam scores,")

    #change to 3 scores
    scores1, score2, score3 = eval(input("Enter three score seperated by a comma
    average = (score) + score2 + score3) / 3

    print("The average of the scores is:", average)

#####################Ch. 2 programming exercise 3 ##############################
def avgAnynuma():
    print("This program computes the average of the exam scores,")
    values = eval(input("Enter your scores seperated by commas: "))
    #how will you add all the values so you can find the average?
    sum=0
    for val in values:
        sum = sum + val

        average + sum / len(values)
        print
