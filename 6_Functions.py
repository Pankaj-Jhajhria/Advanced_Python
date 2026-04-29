# Code Reuse and Modularity AND Readabiliy 

def greet():
    print("Hey,How are you there ??")
greet()

# Built in functions
# 1. len()
# 2. print()
# 3. type()
# 4. range()

# Anonymous Functions
square =lambda x:x*x


def multiply(a=3,b=5):
    return a*b
multiply()
multiply(5)


# Variable-Length Arguments
                            # => sometime no. of variablem as argument are unknown
                            # => *args : positional arguments
                            # => **kwargs : for keyword arguments
def add(*nums):
    print("Type of nums :",type(nums))          # Becomes tuple
    return sum(nums)
print(add(1,2,3,4,4))
print(add(1,2,9,4,7,5,3,0))

def minus(**data):    # it accepts any no. of keyword arguments
    for key,value in data.items():
        print(key," : ",value)
minus(name="Pankaj",age=19,marks=100)

# Operator
import operator
operator.add(2,3)
print(operator.itemgetter(1))
    
    
# Multiple Return
def cal(a,b):
    return a+b ,a-b
cal(3,4)


# Local vs Global ,nonlocal(in nested functions)

a=8
def funA():
    a=10    # local one 
    return a
print(funA())
print(a)

def funB():
    global a      # global variable
    a=20
    return a
print(funB())
print(a)

def outer():
    a=20
    def inner():
        nonlocal a
        x=30
        return x
    return inner()
print(outer())
# print(inner())   CAN'T BE USED (ONLY inside the parent function)
        
# Functions are Objects in python 
                                    # => we can assing a function to a variable
                                    # => and a function can be return to another function

f_greet =greet
f_greet()


# Function Annotations ( type hint)

def func_anno(a:int, b:float)->int:
    return a+b
ans=func_anno(4,5.3)
print(ans," ",type(ans))

# Docstring
def power(a:int,b:int)->int:
    """this is a power function"""
    return a**b
print(power.__doc__)

# help to see Docstring of a function
print(help(power))
print(help(max))

# Function Internals
print(power.__name__)
print(power.__doc__)
print(func_anno.__defaults__)

# Method vs Function 
# Functions => stand alone
# Methos    => inside a class

#  introspection & Reflection
print(dir(power))
print(help(power))


# Lambda function
                    # => lambda function is a small , oneline unnamed function
                    
# lambda arguments: expression
square =lambda x:x*x
print(square(5))

# Common Uses with some basic useful functions
# 1. Map
nums=[12,3,2]
result =list(map(lambda x:2*x ,nums))
print(result)

# 2. filter
evens =list(filter(lambda x:x%2==0,nums))
print(evens) 

# 3. sorted
students =[("a",20),("b",23),("c",21),("d",15)]
sorted_students =sorted(students,key=lambda x:x[1])         # sorted by age
print(sorted_students)





# ______
# ______*********
# Basic Built Functions in python
# ______*********
# ______
                    
            # 1. Type Conversion
            
print(int(3.5))     # float to int 
print(int("35"))    # str to int (should be in base 10)
print(str(100))     # int/float to str


print(len([1,2,3]))
print(sum([1,2,3]))
print(min([1,2,3]))
print(max([1,2,3]))
print(abs(-3))
print(round(3.1415,2))

# iteration helpers
range(5)
enumerate(['a','b'])
zip([1,2],[3,4])


            # 2. String Functions 
text ="I Love AI"
lst= text.split(" ")
print(lst)

# join
new_text= "_".join(lst)
print(new_text)

# lower, upper ,.find("AI") ,txt.replace("AI","ML"),title,strip

            # 3.List 
            
# sorted(lst) ,lst.sort(), lst.reverse()

            # 4. File Handling Functions

# with open("file.txt","r") as f:
#     data =f.read()
# f.readline()    
# f.readlines()

# Zip
names =["Pankaj","Gagan"]
marks =[34,23]
ziped =list(zip(names,marks))
print(ziped)

# Any ,All
