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
    print("Hello ", sname, ". Your overall exam percentage is as follows: ")
    overallScore = hscore + ascore + fscore
    maxscore = homework100 + assesment100 + finalexam100
    percentage = float((overallScore/maxscore)*100)
    percentage = format(percentage, '.2f')

    return percentage


def GradeFunction():
    return grade


grade_percentage = GradePercentage(studentName,homeworkScore,assessmentScore,finalExamScore)
print(grade_percentage, "%")
