story="once upon a time there was a youtuber named Harry who uploaded python course with notes"
print(story)

#string functions
'''1.len() :function returns the length of the string'''
print(len(story)) 

'''2.endswith() :function returns the boolean value whether the variable string ends with string "xyz" or not'''
print(story.endswith("notes")) #it return true
print(story.endswith("xus")) #it return false

'''3.count() :it return the total number of occurance of a character'''
print(story.count("o"))
print(story.count("a"))
print(story.count('course'))

'''4.capitalize() : it capitalizes first character of string'''
print(story.capitalize())

'''5.find(): it finds a word and return the index of first occurance of that word in the string'''
print(story.find("Harry")) 

'''6.replace(oldworld,neworld) :this function replaces the oldword with newword in the entire string'''
print(story.replace("Harry", "Vaibhavi"))

