letters = ["a", "b", "c", "d"]
matrix = [[0,1], [2,3], [3,5]]
zeros = [0]*10

combined = zeros + letters

numbers = list(range(20))

chars = list("hello world")
print(len(chars))


# access items in list
print(letters[-1])
print(letters[::-1])


# unpacking
numbers = ["Banana", 45, True, 3.14]
name, price, *others = numbers
print(others)

#packing
def multiply(*params):
    return params

myfunk = multiply(23, 44, 64, 34, 3534, 994)

#enumerate function
names = ["java", "python", "C++", "ruby"]
for index, name in enumerate(names):
    print(index, name)

#list function: append(item), pop(index), extend(), sort(), index(), 
# copy(), count(), clear(), insert(), remove(), reverse()

names.insert(2, "Javascript")
print(names)
# names.pop(3)
# names.remove("python")
del names[0:2]
print(names)
names.clear()
print(names)


