def inputGrades(nm):
    grades=[]
    for i in range(0,nm,1):
        grd=float(input('Please enter your grade: '))
        grades.append(grd)
    return grades
def printGrades(nm,x):
    for i in range(0,nm,1):
        print(x[i])
def averageGrades(nm,x):
    average=sum(x)/nm
    return average
def highLow(nm,x):
    highG=max(x)
    lowG=min(x)
    return highG,lowG

numGrades=int(input('How many grades do you have: '))
myGrades=inputGrades(numGrades)
print('Your grades are: ')
printGrades(numGrades,myGrades)
avg=averageGrades(numGrades,myGrades)
print('Your average is ',round(avg,1))
highG, lowG=highLow(numGrades,myGrades)
print('Your high grade is ',highG)
print('Your low grade is ',lowG)