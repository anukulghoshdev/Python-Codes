"""
def greet(name: str) -> None:
    print(f'Hello, {name}')

greet("Anukul")
greet("Ludic")

def add (a: float, b: float):
    return a + b
 
print(add(2,3))
"""

def evenOdd(x):
    if (x % 2 ==0):
        return "Even"
    else:
        return "Odd"
    
print(evenOdd(14))
print(evenOdd(43))


def myFunc(*args):
    for arg in args:
        print(arg)

myFunc('hello', 'Ban', 'people', 34)


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))



def fun(**kwargs):
    # print(**kwargs) 
    print(kwargs) 
    for k, val in kwargs.items():
        print(k, "=", val)
fun(s1='Python', s2='is', s3='Awesome')


def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ":" +  str(v))

    return ", ".join(details)

print(introduce(Name="sdf",age=34, City="new york" )
