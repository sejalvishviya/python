myDict ={
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are", myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present.
print("The meaning of your word is:", myDict.get(a))