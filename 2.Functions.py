# Functions
#* Functions are the reusable block of code that performs a specific task.


#1. In python they are defined using 'def' key word

#------------------Example 1--------------------

def my_function():
    print('Hello World')

my_function()  # calling the function to get the result in output.




#2. Arguments/args in Functions
# arguments are specified after function name 

#-----------------Example 2-----------------------

def my_function_1(fname): #function having one argument that is fname
    print(fname + ' ' +'Baidhya')

#calling the function
my_function_1('Shubham')


#---------------Example 3--------------------------

def myfunction_2(f_name,l_name):
    print(f_name+' '+l_name)

myfunction_2('Shubham','Baidhya')




# Arbitary Arguments ,*args
# if the number of arguments that will be passed into our function is unknown, add a * before parameter name

#-------------Example 4--------------------------

def myfunction_3(*kids):
    print('The youngest child is'+" "+ kids[2])# can access accordingly

myfunction_3('Ram','Shyam','Hari') #tuple of arguments


#Keywords arguments (sending arguments with the key= value syntax)

def my_function4(child3, child2, child1):
    print('The youngest child is'+ ' ' + child3)


my_function4(child1='Ram',child2='Shyam',child3='Hari')




# Arbitary Keyword Arguments (**args)

#----------------Example 5------------------------
def my_function5(**kid):  # **kid is the  keyword variable-length argument.

    print('The youngest child is:'+' '+ kid["l_name"] ) 

my_function5(f_name="Ram",l_name="Thapa") #these are the keyword argument and the kid parameter collects these keyword arguments as a dictionary
# here f_name and l_name are the keys 
# and they are called in as a string inside the array of the parameter kid that collects the values residing inside the key.



# Default Parameter Value 
#=> giving a default value to the argument

#-----------------Example 6------------------------

def my_function6(country='Nepal'):
    print('I am from:'+' '+country)

my_function6('Norway')
my_function6()
my_function6('England')


# Passing a list as an Argument
#=> we can send any data types of argument to a function and it will treat it likewise.

#--------------------Example 6----------------------

def my_function7(food):
    for x in food:
        print (x)

fruits=["apple","banana","peach"] 

my_function7(fruits)


# Return Value

#-----------------Example 7------------------------
def my_function8(x):
    return x*5

print(my_function8(2))