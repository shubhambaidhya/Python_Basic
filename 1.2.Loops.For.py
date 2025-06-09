#  Loops => it is used for iterating over a sequence (that is either a list, tuple, a dictionary, a set or a string)
#  Types => For Loop
#        => While Loop


# 1. For Loop

#----------------Example 1-------------------
fruits = ['apple','banana','cherry']
for x in fruits:
    print(x)

# with the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#------------------Example 2-------------------
# looping through the letter of string
for x in 'banana':
    print(x)

# Break Statement => we can stop the loop before it has looped through all items:

#------------------Example 3-------------------
tools = ['hammer','nails','Screw driver']
for x in tools:
    print(x)
    if x=='nails':
        break


# range() function => to loop a set of code a specified number of times, we can use the range() function
# it returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) and ends at a specific number

#--------------------Example 4--------------------
for x in range(6):
    print (x)     # the values from 0 to 5 are given as the output.

#we can also specify the starting value by adding a parameter

#-------------------Example 5---------------------
for x in range(2,6):
    print (x)

#the default increment of range function is 1 but we can also specify the increment value by adding an another parameter

#-----------------Example 6------------------------
for x in range(2,30,3):
    print (x)           # the values from 2 to 30 in incremented each time by 3


# Else in For Loop

#-----------------Example 7-----------------------
for x in range(6):
    print (x)
else:
    print("Finally Finished")

#when break statement is used

#----------------Example 8------------------------

for x in range(6):
  if x == 3: break  #if the loop breaks, the else block is not executed 
  print(x)   
else:
  print("Finally finished!")



#Nested Loops => A nested loop is a loop inside a loop

#-----------------Example 9------------------------
adj = ['red','big','tasty']
fruits=['apple','banana','cherry']

for x in adj:
    for y in fruits:
        print(x,y)
