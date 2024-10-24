'''Q7. Write a program to find out whether given post is talking about Harry or not'''

statment=input("Enter the sentence :")


str1 = "harry"

if  str1 in statment:
    spam= True

elif str1.upper() in statment:
    spam=True

elif  str1.lower() in statment:
    spam=True

elif str1.capitalize() in statment:
    spam=True

elif str1.casefold() in statment:
   spam=True

else:
    spam= False

if (spam) :
    print("This post is talking about the Harry")

else:
    print("This post is not taling about harry")