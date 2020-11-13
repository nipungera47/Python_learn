# This full page is dedicated to strings


a=40
b="Nipun"

print(a,b)
print(type(b))

#The reason and implementation why single,double  and triple quotes are used

c="ni'pun'nfns"
print(c)

d=''' ""My name is nipun gera "'''
# so here we can see the double and single quotes are printed when we execute the program.....
print(d)




#STRING CONCATINATION....

str1="Good morning"
str2="How are you"

print(str1 + str2)


# STRING SLICING ...

name="nipun"

print(name[0])

print(name[1])

print(name[2])

print(name[3])

print(name[4])


print(name[0:3])

print(name[1:4])

print(name[:3])  # it will automatically replace the blank place with the 0 index here!!

#similar if we leave end index blank then we will have the string printed from the starting index till the end index..

print(name[1:]) # OUTPUT WILL BE ipun  same as [1:N-1]...

#Negetive indices are also used for slicing of the string

print(name[-5:-1]) # here we will get ___name[0:4]___ in the output ....


#slicing using skip value ....
print(name[1:2:5])


#2nd example

name1="MynameisNipunGera"

e= name1[1:7:2]

print(e)





# String Functions

str3="i am a very good boy"

print(len(str3))

print(str3.count("a"))

print(str3.endswith("boy"))  #this will give answer in the form of boolean

print(str3.capitalize())

print(str3.find("very"))  # this will find theword if it is there

print(str3.replace("very","asdf"))  # this will replace the word
