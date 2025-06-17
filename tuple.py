# ordered, immutable, allows duplicate values
# iterable, indexable

my_tuple = (0,1,2,3)
# print(my_tuple)

t1 = (1,2,3,4)
t2 = (1, "hello", 3.14, True) # multiple item tuple
t3 = (5,) #only one item, but must be comma(,)
t4 = tuple([1,2,3,4])

# accessing tuple
t = (10, "anukul", 4.75, True)
# print(t[1])
# print(t[3])
# print(t[-1])

# run loop in a tuple 
for item in t:
    print(item)

# some build-in functions 
# print("tuple size is: ",len(t))
# print(t.count("anukul"))
# print(t.index(4.75)) # come value error when item isn't exit in the tuple

# list mutable, tuple immutable
my_list = [1,2,3,4]
my_list[3] = 10
my_list.append(34)
my_list.remove(1)
# print(my_list)

tup = (1,3,4,5)
print(tup[3])
tup[3] = 34
print(tup) # TypeError: 'tuple' object does not support item assignment

