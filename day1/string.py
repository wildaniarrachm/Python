#How to declare variable and its value on python

string = "Hello, Wildan!"
print (string)

x = str('Hello, Zaka!')
print(x)

#to know the data type of a variable
print (type(x))

# You can assign a multiline variable by using three double quotes or three single quote
#1. Using three double quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#2. Using three single quote
A = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(A)

#the positioning of the characters started from index 0
# 0 -> B, 1 -> a
fruit = "Banana"
print(fruit[4])

#Looping through a string

for x in fruit:
    print(x)

for x in "Zaka":
    print(x)


#String Length
# to get the length of a string, use len() function

words = "Hello Darkness My Old Friend"
print(words)
print(len(words))

#Check if NOT (return-> boolean)
txt = "I will be the best version myself this year"
print("worst" not in txt)

#with if statement

if "worst" not in txt:
    print("No, Things will get better!")

#Slicing -> to return a range of characters by using the slice syntax
#example below: the return should be llo 
text = "Hello, World!"
print(text[2:5])

# [2:5] means that the sliced characters started at index 2 to index 5
# while the rest of the characters will not be included.

#slicing from the start
print(text[:5])
#[:5] means that the slicing started at index 0 to index 5

#slicing to the end
print(text[2:])
#[2:] -> slicing started at index 2 to the last index

#negative slicing -> the indexing started from the end of the string

print(text[-5:-2])