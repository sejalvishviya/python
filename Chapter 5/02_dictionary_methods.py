myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A coder",
    "Marks":[1, 2, 4],
    "anothherdict":{'harry':'Player'}
}

# Dictionary Methods
print(list(myDict.keys())) # Printy the keys of the dictionary
print(myDict.values()) # prints the keys of the dictionary
print(myDict.items()) # Print the (key,value) of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # Prints value associated with key harry
print(myDict["harry2"]) # Prints value associated with key harry

print(myDict.get("harry")) # Gives none as harry2 is not present in dictionary
print(myDict["harry2"]) # throws error as harry2 is not present in dictionary