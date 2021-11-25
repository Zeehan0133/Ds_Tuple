"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : remove an item from a tuple
"""
"""
Description:
      
Parameter:
      
Return:
       
"""
fruits= ("apple","orange","banana")
print(fruits)
list1= list(fruits)
list1.remove("banana")
fruits= tuple(list1)
print(fruits)
