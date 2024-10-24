'''Q2. Write a program to greate all the person names stored in a list l1 and which starts with s'''

l1 = [ "Harry","Soham", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello" +"  "+ name)