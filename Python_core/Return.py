import sys


def add(a, b):

    # returning sum of a and b
    print("Kiran {}".format(a,int))
    return a + b


def is_true(a):

    # returning boolean of a
    return bool(a)


def is_true(a) -> bool:
    #returning boolean of a
    try:
        print(a)
        print(type(a))
        return int(a)
        #raise type_error("input datatype is error")
    except:
            print("error is: ")
            sys.exit()
    finally:
            print("Completed")

def modular(x):
    try:
        result = x/0
    except ZeroDivisionError as e:
        print(e,"error")

# using of retun helps to reduce else statement
def check_age(age):
    if age < 18:
        print("Not allowed")
        return  # Exit early if age is less than 18
    print("Allowed")


def do_something():
    global x
    x = 10 * 2

class Counter:
    def __init__(self):
        self.count = 0  # variable as an attribute

    def increment(self):
        self.count += 2

counter = Counter()
#counter.increment()
print(counter.count)


def process_number(num):
    if isinstance(num, (int, float)):
        return num * 2
    return "Input must be an integer or a float."

print(process_number(5))       # Output: 10
print(process_number(3.2))     # Output: 6.4
print(process_number("hello")) # Output: "Input must be an integer or a float."


# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))
# b = 2
# res = is_true(b)
# print("\nResult of is_true function is {}".format(res))

#modular(10)
check_age(17)

x = 0
do_something()
print(x)
print(x.bit_count())