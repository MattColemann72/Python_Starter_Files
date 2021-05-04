'''
Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.

The program should take the students name, Homework(/25) score, Assessment(/50) score and Final Exam(/100) score as inputs.
Output their name and final ICT grade as a percentage.

Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)
'''

homework100 = 25
assesment100 = 50
finalexam100 = 100

studentName = str(input("Please enter students name: "))
homeworkScore = int(input("Please enter students homework score: "))
assessmentScore = int(input("Please enter students assesment score: "))
finalExamScore = int(input("Please enter students final exam score: "))

def GradePercentage(sname,hscore,ascore,fscore):
    print(f"Hello, {sname}. Your overall exam percentage is as follows: ")
    overallScore = hscore + ascore + fscore
    maxscore = homework100 + assesment100 + finalexam100
    percentage = float((overallScore/maxscore)*100)
    percentage = format(percentage, '.2f')

    return percentage


'''
Create an application which asks the user for an input for a maths mark, a chemistry mark and a physics mark.
Add the marks together, then work out the overall percentage. And print it out to the screen.
If the percentage is below 40%, print “You failed”
If the percentage is 40% or higher, print “D”
If the percentage is 50% or higher, print “C”
If the percentage is 60% or higher, print “B”
If the percentage is 70% or higher, print “A”
'''


def GradeFunction(percentage):
    if float(percentage) < 40:
        grade = "You failed"
    elif float(percentage) < 50:
        grade = "D"
    elif float(percentage) < 60:
        grade = "C"
    elif float(percentage) < 70:
        grade = "B"
    else:
        grade = "A"
    return grade


grade_percentage = GradePercentage(studentName,homeworkScore,assessmentScore,finalExamScore)
grade_letter = GradeFunction(grade_percentage)
print(f"{grade_percentage}%")
print(f"{studentName}, you received a {grade_letter}")