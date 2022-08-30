'''
Created on Aug. 30, 2022

*Find the intersection (common) of two sets and remove those elements from the first set
See: Python Set

@author: Said
'''


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

x =first_set.intersection(second_set)
new_set = first_set - x

'''
for item in intersection:
    first_set.remove(item)
'''
print(new_set)
