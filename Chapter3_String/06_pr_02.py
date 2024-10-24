letter= '''Dear <|Name|>
You are selected!
Date:<|Date|>
'''
name=input("Enter Your name :")
date=input("Enter the date :")

letter=letter.replace("<|Name|>", name)
letter=letter.replace("<|Date|>", date)

print(letter)

