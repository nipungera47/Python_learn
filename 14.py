import  datetime

x=datetime.datetime.now()


print(x)

# To Print Year
print(x.year)

# to print month
print(x.month)

# this strftime is the funtion to format string  and give us what we require.
print(x.strftime("%B"))