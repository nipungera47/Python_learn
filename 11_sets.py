a={1,3,4,5} # Sets doesnot have repetetive items as define says collection of non-repetetive items
print(a)
print(type(a))

# tHIS Syntax
# b={}
# will not  create an empty set rather it is a dictionary if see its type


#An empty set is created using this syntax
b=set()
print(type(b))
b.add(4)
b.add(6)

print(b)

# We cannot add list inside the set but we can add tuple in the list
#
# b.add([1,2,40])
# b.add({1,2,4}) # we cannot add dictionary in the set because dictionary is not hashable


# we can check the length using  len function
print(len(b))

# also we can remove using remove function
b.remove(6)
print(b)


#Pop() function removes removes on element from the set

b.pop()
print(b)