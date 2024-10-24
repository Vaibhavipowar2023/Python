'''Q1. Write a program to find greatest of four numbers enterd by the user'''

# num1 = int(input("Enter number1 :"))
# num2 = int(input("Enter number2 :"))
# num3 = int(input("Enter number3 :"))
# num4 = int(input("Enter number4 :"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("Num1 is greater:",num1)
# elif(num2>num1 and num2>num3 and num2>num4):
#     print("Num2 is greater:",num2)
# elif(num3>num1 and num3>num2 and num2>num4):
#     print("Num3 is greater:",num3)
# else:
#     print("Num4 is greater :",num4)

'''OR'''


num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
num3 = int(input("Enter number3 :"))
num4 = int(input("Enter number4 :"))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(str(f1)+" Is greatest")
else:
    print(str(f2)+ "is greatest")

