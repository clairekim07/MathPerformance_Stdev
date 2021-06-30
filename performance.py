import statistics
import csv
import pandas as panda
import plotly.figure_factory as ff

score = []
with open("performance.csv", newline = '') as data:
    read = csv.reader(data)
    newList = list(read)
    newList.pop(0)
    students = len(newList)
    print("Students: " + str(students))
    for total in range(0,students):
        for math in newList:
            score.append(float(math[5]))
    
mean = statistics.mean(score)
print("Mean: "+str(mean))

median = statistics.median(score)
print("Median: "+str(median))

mode = statistics.mode(score)
print("Mode: "+str(mode))

std = statistics.stdev(score)
print("Standard Deviation: "+str(mean))

firstStdStart, firstStdEnd = mean - std, mean + std
secondStdStart, secondStdEnd = mean - (2 * std),mean + (2 * std)
thirdStdStart,thirdStdEnd  = mean - (3 * std),mean + (3 * std)
firstNum = 0
secondNum = 0
thirdNum = 0
for i in range(0,students):
    if score[i] >= firstStdStart and score[i]<=firstStdEnd:
        firstNum += 1
    if score[i] >= secondStdStart and score[i]<=secondStdEnd:
        secondNum += 1
    if score[i] >= thirdStdStart and score[i]<=thirdStdEnd:
        thirdNum += 1
firstStdPercentage = firstNum/students
firstPer = "{:.2%}".format(firstStdPercentage)
print("First Stdev percentage: " + str(firstPer))

secondStdPercentage = secondNum/students
secondPer = "{:.2%}".format(secondStdPercentage)
print("Second Stdev percentage: " + str(secondPer))

thirdStdPercentage = thirdNum/students
thirdPer = "{:.2%}".format(thirdStdPercentage)
print("Third Stdev percentage: " + str(thirdPer))

nCurve = ff.create_distplot([score],["Math score"], show_hist=False)
#nCurve.show()