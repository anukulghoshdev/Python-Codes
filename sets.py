# unordered, unchangeable, unindexed, no duplicates
# same datatypes

# Once a set is created,it cannot be changed, but we can add new items to it.
# can add new items
myset = {"apple", "banana", "cherry"}
print(myset)
print(len(myset))
print(type(myset))

thisset = set(("2", "4", "6"))
print(thisset)


# acces set items 
for x in thisset:
    print(x)    

print("banana" in myset)
print("banana" not in myset)

myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)

myset.update(thisset)
print(myset)
print("after updating:", myset)

#remove item
myset.remove("banana")
print(myset) # if item does not exist, it will raise an error
myset.discard("banana") # if item does not exist, it will not raise an error
print("after discard", myset)

myset = {"apple", "banana", "cherry"}
print(myset)
myset.pop() # removes a random item
print("after pop", myset)

myset.clear() # empties the set
print("after clear: ", myset)