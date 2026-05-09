print('\nhello World',end="\nHey There !\n")
print('Pankaj\n')
name ="Pankaj"
age =13
Name ="atul"
Name


# Start with Capital/small letter and underscore(-) 
# and can be used numerical digits in further       :Variables

"""my name is pankaj
alsdlljdgljld"""

# How for iterator loop works:

def my_own_loop(iterable):
    try:
        iterator=iter(iterable)
    except TypeError:
        print("This  variable is not iterable.")
    else:
        while True:
            try:
                print(next(iterator))
            except StopIteration:
                break
            # print(next(iterator))
            
L=[1,2,3,4]
D={"name":"pankaj","age":20}
S={1,2,3}
A=23
my_own_loop(L)
my_own_loop(D)
my_own_loop(S)
my_own_loop(A)

# id(iter(iterable)) =id(iter(iter(iterable)))

class my_own_range:
    
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
    
    def __iter__(self):
        return my_own_iterator(self)
    
class my_own_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj
    
    def __iter__(self):
        return self
    def __next__(self):
        
        if self.iterable.start >=self.iterable.end:
            raise StopIteration
        
        current=self.iterable.start
        self.iterable.start+=self.iterable.step
        return current
    
for i in my_own_range(12,23,1):
    print(i)
print()

    
my_own_loop(my_own_range(12,23,1))
