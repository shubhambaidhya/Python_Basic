#While Loop =>  with while loop we can execute a set of statement as long as the condition is true.

#------------------Example 1-------------------------

i=0
while i<6:
    print(i)
    i+=1

#* Remember to increment i, or else the loop will continue forever.


# Break statement => the break statement can stop the loop even if the while condition is true,
#--------------------Example 2-----------------------

i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1


#continue Statement => this statement can stop the current iteration, and continue with the next
#---------------------Example 3--------------------------

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)

#else statement => With the else statement we can run a block of code once when the condition no longer is true.
#----------------------Example 4---------------------------
i=1
while i<6:
    print(i)
    i+=1
else:
    print('i is no longer less than 6')

