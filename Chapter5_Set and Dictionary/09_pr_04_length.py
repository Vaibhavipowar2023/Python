'''Q4. what will be the length of following set s'''

s=set()
print(s)
print("Length of empty set :",len(s))

s.add(20)
print(s)
print("Length of set when we add 20 :",len(s))

s.add(20.0)
print(s)
print("Length of set when we add 20.0 : ", len(s))

s.add("20")
print(s)
print("Length of set when we add 20 : ", len(s))