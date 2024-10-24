greeting="Good morning , "
name="Vaibhavi"

print(greeting + name) #concatenate two string we use + sign

#how to give the index number of string

'''Index sart from  0'''
print(name[0])
print(name[4])

#print(name[9])# IndexError: string index out of range

#name[4]="p" -->Does not change


'''slicing'''
print(name[0:3]) #it gives character 0 to 3 letter such as Vai it does not give 3rd index

print(name[:-2]) #negative index is use to find the length of the string

print(name[:8]) #is sane as name[1:5]

print(name[1:])#is same as name[0:8]

print(name[-4:-1]) #is same is name[1:4]



# Slicing syntax:[start:stop:step]
d=name[1:7:1] #it print skip 1 value
print(d)