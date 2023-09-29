# data types in python 

# 1. interger 
# 2. boolean  TRUE OR FALSE SITUATION
# 3. float  DECIMALS I.E 16.02
# 4. complex    this is a mixtures of intergers and strings i.e 14k + 10
# 5. string   sequences of characters i.e "abcdefghijklmnop"

# interger types

# childAge = 17;

# print(childAge); # this should print the child age 17

# print(type(childAge)) # this should print the data type of childAge that is interger type.

# #  boolean

# isMarried = True;

# print(isMarried);   # this should   be TRUE

# print(type(isMarried)) # this should print the  data type of isMarried that is  boolean type.

# # float 

# height = 1.80;

# print(height); # this should print the height 1.80

# print(type(height)) # this should print the data type of height that is float type.

# # complex     

# complexNumber = 14 + 10j;

# print(complexNumber); # this should print the complex number 14 + 10j

# print(type(complexNumber)) # this should print the data type of complexNumber that is complex type.

# # string

# name = "<NAME>";

# print(name); # this should print the name "<NAME>"

# print(type(name)) # this should print the data type of name that is string type.

# assignment 

x = 75;

def myfunc():
    x=x+1
    print(x);
    
    myfunc()
    print(x)
    
    
    # this should print 76. or error
    # 
    print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
    
    from datetime import datetime
    
    day = datetime.today();
    parsecs = 11

lightyears = parsecs * 3.26

print(str(parsecs)+ " parsecs is " + str(lightyears)+"lightyears") 

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
    
    #  the input() function stores a result as a string
    
    #  if the user writes integers instead of strings then the output will add the 1st and 2nd integer  i.e user writes 24 then last_name 12 the output will be 2412 instead of 36;
    # otherwise if you want it to write the output as 36 you need to add int() function;
print ("Running Out of Date")

first_name = input("First Name:")

last_name = input("Last Name:")

print(first_name + " " + last_name)

first_name = input("First Name:")

last_name = input("Last Name:")

print(int(first_name + " " + last_name))

#  or

print(int(first_name) + int(last_name))


    
    