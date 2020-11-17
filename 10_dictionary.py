#Dictionary is a key value pair.
#We can have list and string values in a dictionary.
dict={
    "fast":"quickly",
    "nipun":"a good boy",
    "usa": "america",
    "list":[1,2,4],
    "inside_dict":{ 'a':'1','b':'2'}
}
# We ca also have one dictionary in the dictionary itself.......
print(dict)

print(dict['fast'])
print(dict['usa'])
print(dict['list'])

print(dict['inside_dict'])
print(dict['inside_dict']['a'])
# Dictionary methods

print(dict.keys())  # This will print keys of the dictionary
print(type(dict.keys()))

print(dict.values())


print(dict.items()) # Print keys,value for all contents of the dictionary
print(dict)
update={
    "sdds":"afhak"
}
dict.update(update)
print(dict)

print(dict.get("sdds"))  # We use .get() function if we use it , it will return us null where as if we use square bracket it will return error





