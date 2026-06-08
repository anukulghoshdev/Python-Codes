# key value pair, unordered, changeable(mutable),

# all dictionary syntax
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
empty_dict1 = {}
empty_dict2 = dict()
person = dict(name="Karim", age=24, city="Dhaka")
student = {
    "name":"anukul",
    "age": 24,
    "courses": ["Python", "Django", "Javascript"]
}

#access
"""
print(student["name"])
print(student.get("age"))
print(student.get("phone"))
""" #  যদি key না থাকে, error দেবে না get() function এ)

# adding new data
student['phone'] = "01704765585"

#update existing key
student['name'] = "Karim"

# update() - মেথড দিয়ে একসাথে অনেকগুলো ভ্যালু আপডেট: 
student.update({
    "name": "Rakib",
    "age" : 23, 
    "phone" : "01423235234"
})


# delete element
del student['phone']

# delete a item of a dictionary
age = student.pop("age")
print(age)

student.popitem() # delete last item
# student.clear() # make empty dictionary
print(student.keys())
print(student.values())
print(student.items())


# looping dictionary
for key in student.keys():
    print(key)

for values in student.values():
    print(values)

for key, values in student.items():
    print(f"{key}: {values}")

# Dictionary কম্প্রিহেনশন
squares = {x: x*x for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Nested Dictionary
employess = {
    "emp1" : {"name": "Anukul", "age":23}, 
    "emp2" : {"name": "Rossi", "age": 34},
}
print(employess["emp2"]["name"])



almim = {
    "name": "Alauddin",
    "age":13,
    "Roll": 31,
    "class":6,
    "group":"Joba"
}
almim.pop('age')
almim.popitem()
print(almim)

#practice problem
numbers = {
    "১" : "one", 
    "২" : "two",
    "৩" : "three", 
    "৪" : "four", 
    "৫" : "five"
}
del numbers['৩']
print(numbers)

for key, values in numbers.items(): 
    print(f"{key} -> {values}")
