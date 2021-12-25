# 5. Write a Python program to print a specified list after removing the 4th elements.

LST = ["abc", "123","5","6","7"]

LE = []

for i in range(len(LST)):
    
    if i == 4:
        continue
    else:
        LE.append(LST[i])
print(LE)