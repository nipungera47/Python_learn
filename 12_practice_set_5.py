# This is Practice set 5
#Q1 find word from dictionary


dict={
    "meetha": "chocolate",
    "pyarr":"love",
    "television":"tv"

}

print("The options are :",dict.keys())
a=input("Enter the word: ")
print("MEaning of the word is:",dict.get(a))