'''
Created on Aug. 25, 2022

*Create a list by picking an odd-index items from the first list and even index items from the second


@author: Said
'''
from multiprocessing.dummy import list

'''
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''


'''
ist = [3, 6, 9, 12, 15, 18, 21]
list = [4, 8, 12, 16, 20, 24, 28]
list1=[]


print(ist[1::2])
'''

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

    