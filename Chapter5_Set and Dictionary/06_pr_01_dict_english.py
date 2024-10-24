'''Q1. Write a program to create a dictionary of hindi word with values as their 
english translation provide user with an option to look it up'''

mydict={
    "Pankha"  : "fan",
    "khurchi" : "chair",
    "Atta"    : "doue"

}
print("Options are :",mydict.keys())
print(" ")
a=input ("Enter the Hindi word :\n")

#below line will not throw an error if the key is not present in dictionary
print("The meaning of your word is :",mydict.get(a)) #by using get()

