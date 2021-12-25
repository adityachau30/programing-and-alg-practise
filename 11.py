# 11. Write a Python program to remove an item from a set if it is present in the set.

integer = {1, 2, 3, 4, 5, 6}

a = int(input("enter a number to remove number"))

b = 0

for item in integer:
    
    if item == a:
        
        integer.remove(a)
        print(f"The Modified set after removing {a} is : {integer}")
        break
    
    else:
        b = b+1

if b == len(integer):
    print(f"{a} is Not found in Set : {integer}")