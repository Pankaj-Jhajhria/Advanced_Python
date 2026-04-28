# Sets (Unordered ,Mutable ,Unique)

seet ={1,3,3,5,2}   #remove duplicated autometically
print(seet)
seet=set([1,3,3,5,2])
print(seet)

# empty set
empty_one=set()
print(empty_one)

# elements should be immutable
# seet ={1,3,[3,4,5],{1:3}}     gives error because of list and dictionaries as elements of the set
seet.add(34)
print(seet)

#   Remove elements
seet.remove(3)     # Gives error      
seet.discard(3)    # Doesn't Gives error
seet.pop()         # removes a element randomly
print(seet)

