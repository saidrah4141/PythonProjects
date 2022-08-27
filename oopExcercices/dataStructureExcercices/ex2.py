'''
Created on Aug. 26, 2022

* Write a program to remove the item present at index 4 
and add it to the 2nd position and at the end of the list.

@author: Said
'''
list1 = [54, 44, 27, 79, 91, 41]

# List After removing element at index 4  [34, 54, 67, 89, 43, 94]
# List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
 #List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
 
list1.append(list1[4])
list1.pop(4)
list1.insert(2, list1[-1])
print(list1)

'''
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

sample_list.append(element)
print("List after Adding element at last ", sample_list)
'''