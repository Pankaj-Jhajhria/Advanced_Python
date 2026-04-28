List=["Pankaj",34,1.3,True]
print(List)
print(type(List))
print(type(List[0]))
print(type(List[1]))
print(type(List[2]))
print(type(List[3]))

# Indexing
name="Pankaj"
print(List[0])
print(List[-3])

# Append
List.append("Aman")
List.insert(2,"Akash")
List.extend([2,4,2])   #multiple items
# List.append(List.copy())
# List.insert(2,List.copy())   # Both works
print(List[2][2])
print(List)


List.insert(45,"akash")    # if index exceds than just append to the last
print(List)

# Remove
List.remove("Aman")
List.pop(3)
print(List)
# List.pop(23)                  #Error

List.append("Pankaj")
print(List)
List.remove("Pankaj")
print(List)
# List.remove("Rahul")           #Error
print(List)

# Memborship Checking
print("Pankaj" in List)

# Variable object similarity in memory rather than their values
print(List is name)

# Others
print(len(List))
print(List.count("Pankaj"))
print(List.index("Pankaj"))

# Copying in new list
List2=List.copy()

print(List2.count("Panka"))        # No Error if not available
# print(List2.index("34"))           # gives error if not available
print(List2.clear())      # remove all elements
print(List2)

# None datatype
print(type(None))
print(List)


# Sorting the list 
print([23,45,2,24].sort())
List2=[23,45,2,24]
List2.sort(reverse=False)
print(List2)
# print(List.sort())  #datatypes should be same(like numbers ,or str)
print(List.reverse())     #returns None and reverse the original one only
print(List)

List2=list((1,2,3))
print(List2)

# Slicing
List2 =List[1:3]
print(List2)

# Modification
List[2]=False
print(List)

# del 
del List[2]
print(List)

List3 =List[:2]
# List3=List3.sort(key=lambda x:len(i) )
print(List3)


#  Nested lists(Matrix,2D List)
# print(max(List))         # ,min,sum()

