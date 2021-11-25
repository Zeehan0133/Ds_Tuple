"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : program to find the repeated items of a tuple
"""
"""
Description:
     
Parameter:
      
Return:
       
"""
my_tuple = (1, 1, 2, 3, 4, 4, 5)
repeated_items = []
for i in my_tuple:
    if my_tuple.count(i) > 1:
        repeated_items.append(i)
print(set(repeated_items))
print(repeated_items)
