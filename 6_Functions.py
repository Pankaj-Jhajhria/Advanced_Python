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
def add(*nums):
    return sum(nums)

# Operator
import operator
operator.add(2,3)
print(operator.itemgetter(1))

# f\