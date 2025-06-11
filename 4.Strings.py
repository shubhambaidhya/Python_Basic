# Strings => strings in python are surrounded by either the single quotation or double quotation marks.
# Eg: 'Hello' / "Hello"

#Strings as an Array
#* Python doesn't have a character datatype so, a single character is simply a string with length 1

#------------------Example 1-------------------------

a ='Hello World!'
print(a[1]) #the output is e cause the first index starts with 0



#Check String => we can use keyword 'in' to check if a certain phrase or character is present in a string or not 

#-------------------Example 2--------------------------

txt = 'The best things in life are free!'
if "free" in txt:                       # used if statement as well
    print("Yes, 'free' is present.")


#Slicing Strings => You can return a range of characters by using the slice syntax

#-------------------Example 3-------------------------

b="Hello World!"
print(b[2:5])


#Slice from the start
#------------------Example 4-------------------------

b="Hello World!"
print(b[:5])    #Get the characters from the start to position 5 (not included)


#-----------------Example 5---------------------------

b="Hello World!"
print(b[-5:-2])


#strip() method => removes any whitespace from the beginning or the end:

#-----------------Example 6--------------------------
a=' Hello, World! '
print(a.strip()) #removes the white space before and after the text


#split()  method => splits the string into substring if it finds instances of the separator:

#-----------------Example 7--------------------------
a = 'Hello, World!'
print(a.split(',')) 



# String Format 

# we will find the error in the below commented code 

#age=36
#txt='My name is John, I am'+age
#print (txt)

# To resolve this error, 'F' string was provided in Python => To specify string as an f-string, simply put 'f' in front
# of the literal string, and add curly brackets  {}  as a placeholder for variables and other operation

#------------------Example 8---------------------------
age =35
txt = f'My name is John, and I am {age} years old'
print(txt)



