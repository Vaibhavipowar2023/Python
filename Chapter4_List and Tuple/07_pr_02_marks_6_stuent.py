'''Q2 Write a program to accept marks of 6 students and display them in a sorted manner'''
s1=int(input("Enter the 1st student marks :"))
s2=int(input("Enter the 2nd student marks :"))
s3=int(input("Enter the 3rd student marks :"))
s4=int(input("Enter the 4th student marks :"))
s5=int(input("Enter the 5th student marks :"))
s6=int(input("Enter the 6th student marks :"))

student_marks=[s1,s2,s3,s4,s5,s6]
student_marks.sort()
print(student_marks)