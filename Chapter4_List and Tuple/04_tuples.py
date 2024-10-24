'''tuple is a unmutable 
we can't change value'''
#creating empty tuple
tuple2=()
print(tuple2)

#creating tuple with single element
t2=(1,)
print(t2)

#wrong way of creating tuple with single element
t3=(1) #it assume that it is number
print(t3) 


#creating a tuple using ()
tuple1=(1,2, 4,5,2)
print(tuple1)

#printing the elements of a tuple
print(tuple1[0])

#cannot update the values of a tuple
tuple1[0] = 34
print(tuple1)