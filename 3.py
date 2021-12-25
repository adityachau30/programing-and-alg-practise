# 3. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample: list1 = [‘aba’,’121’,’kgf’,’abc’]

list = ['aba','121','kgf','abc']
total = 0
for i in range(0, len(list)):
    
    a = list[i]
    
    if len(a) >= 2:
        '''Assigned First Character of String to first and lst character
         of string to last respectively '''
        first = a[0]
        last = a[len(a) - 1]
        
        if first == last:
            total = total + 1

print(f"The Number of string having first and last character same and string length 2 is : {total}")

