
#List_Sorting



list=[1,4,2,5,23,43,12,43]
print(list)

# this function will sort the list
list.sort()

print(list)
# this function will reverse the list
list.reverse()
print(list)

#this function will append the list

list.append(3)
print(list)  # you can see in the output that  3 is added at the back of the list


# insert() function is used to insert value at an index

list.insert(2,23)
print(list)


# pop fuction is used to delete the value at an index in the list


list.pop(2) # value is deleted which is at the index 2

print(list)

# this will remove 43 from the list
list.remove(43) 
print(list)