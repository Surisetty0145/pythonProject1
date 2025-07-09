import sys


def add(x,y):
    j = x+ y
    if x is y:
        print("no records")
        return j
        sys.exit()

    else:
        print("")


k = add(5,5)

print(k)

# list comprehension

lst = [x**2 for x in range(5)]
print(lst)


lst1 = [x**2 for x in range(10) if x % 2 == 0]

print(lst1)
