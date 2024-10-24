'''Q7. Write a program function to remove a given word from a string and strip if at the same time'''

#strip function is used to remove the  extra spaces 

def remove_split(string, word) :
    newstr = string.replace(word, "")
    return newstr.strip()


sentence = "     hello vaibhavi , how are you     "
n= remove_split(sentence, "vaibhavi")
print(n)


