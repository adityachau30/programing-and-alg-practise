# 15. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

dict = {}
#For loop to go in every number from 1 to 15
for i in range(1, 16):
    #assigned Numbers as key and their square as Values
    dict[i] = i * i

print(dict)