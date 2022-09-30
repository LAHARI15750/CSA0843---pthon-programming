print("Enter Marks Obtained in 5 Subjects: ")
markOne = float(input())
markTwo = float(input())
markThree = float(input())
markFour = float(input())
markFive = float(input())

total = markOne + markTwo + markThree + markFour + markFive
percentage = (total / 500)* 100

print("total marks = %.2f" %total)
print("marks percentage = %.2f" %percentage)


if   (percentage>=80):
 print("Your Grade is A")
elif (percentage>=50):
 print("your grade is B")
elif (percentage < 50):
 print("your grade is c")
else:
 print("Invalid Input!")



