# ordered
# changeable
# do not allow dublicates
# allow different data types: String, int, boolean, and list data types:
myDict = {
  "brand" : "Ford",
  "model":"Mustang",
  "year": 1964,
  "electric": False,
  "colors": ["red", "white", "blue"]
}

print(myDict)
print(myDict["brand"])
print(len(myDict))

myDict2 = dict(name = 'john', age = '36', country = 'Norway')
print(myDict2)

# access
print(myDict2["name"])
print(myDict2.get("name"))

# get keys
x = myDict2.keys()
print(x)

myDict2["Height"] = 4.5
print(x)
print(myDict2)


















