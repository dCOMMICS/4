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
    
    