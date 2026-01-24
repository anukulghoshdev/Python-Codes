# ordered, immutable, allows duplicate values
# iterable, indexable

my_tuple = (0,1,2,3)
# print(my_tuple)

t1 = (1,2,3,4)
t2 = (1, "hello", 3.14, True) # multiple item tuple
t3 = (5,) #only one item, but must be comma(,)
t4 = tuple([1,2,3,4])
print(t4)

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
# tup[3] = 34
# print(tup) # TypeError: 'tuple' object does not support item assignment

# using enumerate() 
students = ("Anik", "Rifat", "Sumaiya")
for index, name in enumerate(students):
    print(index, name)

# Practice problem 1: find even numbers from a tuple 
t5 = (10,15,22,33,40,55,60)
even_numbers = tuple(i for i in t5 if i % 2 == 0)
print(even_numbers)

# Practice problem 2: find bigger numbers from a tuple 
t6 = (11, 32, 5, 24, 64, 29)
largest = max(t6)
print("Largest Number: ", largest)

# problem 3: tuple reverse 
t7 = (10, 20, 30, 40)
reversed_tuple = t7[::-1] #[start:stop:step]
print(reversed_tuple)

# problem4: add two tuples
t1 = (1,2,3)
t2 = (4,5,6)
combined = t1 + t2 
new_tuple = combined + (5,)
print(combined)
print(new_tuple)

# Remove nested records
test_tup = (1, 5, 7, (4, 6), 10)
print("The original tuple is: ",  str(test_tup))
# for count ele in enumerate(test_tup):

# initialize tuple
test_tup = (1, 5, 7, (4, 6), 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Remove nested records
# using isinstance() + enumerate() + loop
res = tuple()
for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
        res = res + (ele, )

# printing result
print("Element after removal of nested tuple:", res)

# tuple unpacking
t = (2,4,5,6,7)
a,b,c,d,e = t
print(a,b,c,d,e)

#assignment 1: 
tup1 = (3,2,6,4,6)
print(tup1[0], tup1[-1])
for i in tup1:
    print(f"all items {i}")
print(tup1[1:4])

# tuple built-in methods - count(), index()
tu1 = (3, 4, 6, 7)
tu2 = (23, 44, 35, 64)

print(tu1.count(4))   # কতবার 4 আছে
print(tu1.index(6))   # 6 এর index

tu3 = tu1 + tu2         # concatenation
print(tu3)

print(tu1 * 3)        # repeat 3 times

sorted_tuple = tuple(sorted(tu1))  # sorted tuple
print(sorted_tuple)


