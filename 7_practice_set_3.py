# .......This is the practice set 3 .......

import datetime
#Q1.  Display the name entered by user and print name followed by goodafternoon

name=input("Enter Your Name : ")

print("Good Afternoon ", name)


#Q2. Create the template for letter + datetime.datetime.now()
current=  datetime.datetime.now()

print("Dear"+name+"You are selected on date",current )


#Q3. Create the program to find double spaces

str= "i am a  good boy"

s=str.find("  ")

print(s)


#Q4. create a program to replace double spaces to single spaces...

s1=str.replace("  "," ")
print(s1)


#Q5 to print formatted letter or any string

s2="I am a very good boy"

s2_formatted= "I am \n a very \n good boy"

print(s2_formatted)


