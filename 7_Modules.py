# Random

import random
a=random.random()
print(a)

random.seed(42)
b=random.randint(3,33) # generates random values in [3,33]
print(b)

lst=[]
for i in range(10):
    lst.append(random.randint(3,33))
    
print(lst)
random.shuffle(lst)
print(lst)



# Math
import math
print(math.exp(1))
print(math.cos(0))
print(math.log(10))
print(math.factorial(23))


# Time
import time
start=time.time()
print(math.factorial(50))
end=time.time()
print(f"Starting time: {start}\nEnding time: {end}\nTotal time taken: {end-start}")

print(time.ctime())
print(time.localtime())

for i in range(60):
    # time.sleep(0.5)
    print(f"{i} sec")
    
# statistics
import statistics
data=[random.randint(10,100) for _ in range(10)]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.stdev(data))

# collections
from collections import Counter,defaultdict,deque
print(Counter(data))
aa=Counter(data)
print(aa)

defaultdict(int)        # Grouping data

# DateTime
import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())

# OS
import os
print(os.getcwd())
print(os.listdir())


# Json
import json
data={"name":"Pankaj","value":42}
print(json.dumps(data))


# Requesties
import requests
response =requests.get("https://github.com/Pankaj-Jhajhria")
print(response)

# itertools
import itertools

# sys
import sys
n=int(input("Enter your age :"))
if n<18:
    print("Hey Kid ! ,This is not for you.")
    sys.exit('ah ! error !')
print("Tell me how i can help you buddy ??")
