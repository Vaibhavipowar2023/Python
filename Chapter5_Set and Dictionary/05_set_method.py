'''1.set(): creating an empty set'''
b=set()
print(type(b))

'''2.add() : adding values to an empty set'''
b.add(4)
b.add(5)
b.add(5) #adding a value repeatedly does not changes a set
b.add((4,5,6)) #can be add tuples
print(b)

#accessing elements
''' b.add([4,5,6]) cannot add dictionary and list
    b.add({4,6})
'''

'''3.len(): return a length of a set'''
print(len(b))

'''4.remove() remove the element of the set'''
b.remove(5)
print(b)
# b.remove(15) #throws an error while trying to remove 15 (which is not present in the set)
# print(b)

'''5.pop():removed the arbitary element from the set and return the element rmoved'''
print(b.pop())

'''6.clear():Empty the set'''
b.clear()
print(b)

