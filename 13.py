# 13. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary: dic1= {1:10, 2:20} dic2= {3:30, 4:40} dic3= {5:50,6:60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1= {1:10, 2:20}
dic2= {3:30, 4:40}
dic3= {5:50,6:60}
dic4 = {}
#for loop to go in every items of dic1,dic2,dic3 respectively
for i in (dic1,dic2,dic3):
    #update items into dic4
    dic4.update(i)
print(f"The New Dictionary after concatenate {dic1} , {dic2} & {dic3} is: {dic4}")