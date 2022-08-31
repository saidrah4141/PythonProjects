'''
Created on Aug. 26, 2022

*Write a program to iterate a given list and count the occurrence of each element 
and create a dictionary to show the count of each element.

@author: Said
'''


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89,45,11]
list1=[]
occurences={}
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

for i in range(len(sample_list)):
        
    if sample_list[i] in list1:
        occurences.update({sample_list[i]: occurences[sample_list[i]]+1})
    else:
        occurences[sample_list[i]] = 1
    
    list1.append(sample_list[i])


'''
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)
'''



print(occurences)