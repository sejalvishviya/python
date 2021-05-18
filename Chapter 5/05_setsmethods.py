b = set()
print(type(b))

# Adding values to an empty set

b.add(4)
b.add(5)
b.add(4) # can add a no. only 1 time
b.add(5)
b.add((4,5,6)) # Can add tuples to sets
 #b.add({4:5})  # Can not add list or dictionary to sets 

print(b)

print(len(b)) #Prints the length of the set
b.remove(5) # Removes 5 from set
print(b)

print(b.pop()) # Remove a number
print(b)