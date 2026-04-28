# Key-Value Pairs

# Creation
dic ={
    "Names":["Aman","Pankaj","Gagan"],
    "age":[23,19,32]
}
print(dic)

dic2=dict(a=1,b=2)
print(dic2)

dic2=dict([("Name","Pankaj"),("age",19)])
print(dic2)

dic2={x:x**2 for x in range(5)}
print(dic2)

# Accessing Values
print(dic2[3])        # error if out of key 
print(dic2.get(5))    # None if not there 
print(dic2.get(3,0))  # default value if not there


# Adding / Updating Values
dic2[0]=34
dic2[6]=36
print(dic2)
dic2.update({3:45,6:33})    # update maltiple values
print(dic2)


# Removing values
dic2.pop(4)     #error if not there
print(dic2)
dic2.popitem()    #last added item will be removed
print(dic2)
del dic2[3]
print(dic2)
dic2.clear()
print(dic2)


# Methods
print(dic.keys())
print(dic.values())
print(dic.items())

for key in dic:
    print(key)
    
for value in dic.values():
    print(value)
for k,v in dic.items():
    print(k,":",v)

dic.setdefault("Marks",100)   # method in Python dictionaries is a built-in 
# tool that retrieves the value of a specified key or, 
# if the key does not exist, inserts the key with a specified default value
print(dic)

s_dic= {s:len(s) for s in ["Pankaj","Gagan","Himanshu"] if len(s)>5}
print(s_dic)

# Merging two dictionaries
merged_dic= {**dic,**s_dic}
print(merged_dic)
merged2_dic= dic | s_dic
print(merged2_dic)

from collections import Counter
print(Counter("DPankanj"))  # Ascending order and alphabetical order

# Copy and DeepCopy
# ChainMap
# Swap kay-values
rev_dic ={k:v for v,k in s_dic.items()}  #for reverse Values should be immutable
print(rev_dic)

# Grouping Data
from collections import defaultdict
groups=defaultdict(list)
print(groups)
print(type(groups))

sorted(s_dic.items(),key=lambda x:x[0])
print(s_dic)