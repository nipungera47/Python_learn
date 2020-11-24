# we can have two parameters in open or close
# 1st parameter is filename and the other is which operation we have to perform - read,write,append

# file= open("test.txt","r")  opening file in a read mode
# x= file.read()
# print(x)


## Writing into the file


# file= open("test.txt","w")
#
# y=file.write("i am nipun gera")
#
#
# file.close()
#

# Appending text in the file

file=open("test.txt","a")
z=file.write("I will be in a great world one day.")
print(z)


