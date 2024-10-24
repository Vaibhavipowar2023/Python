mydict={
    "name" : "Joy",
    "marks": 96,
    "std"  :"ty"

}
print(type(mydict))# by default type of dictionary :<class 'dict_keys'> we can also change the type


'''1.keys(): it use to print all the keys of the dictionary'''
print(mydict.keys())

'''2.values() :it use to print the values of dictionary'''
print(mydict.values())

'''3.items():it is use to return a list of tuples/print the (key/value)for all the content  of the dictionary'''
print(mydict.items())

'''4.update():updates the dictionary by adding the key-value pairs '''
print(mydict)
updict={"lovish":"friend",
         "player":"football"}
mydict.update(updict)
print(mydict)

'''4.get(): prints value associatied with key '''
print(mydict.get("name"))

#difference between .get and [] syntax
print(mydict.get("name2")) #returns none as name2 is not present in the dictionary
print(mydict["name2"])#thros and error as name2 is not present in the dictionary


