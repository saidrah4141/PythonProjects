'''
Created on Jul. 6, 2022

* prints even index of a string

@author: Said
'''
from _operator import length_hint



'''
name="shyrak"
i=0
while i < len(name):
    print(name[i])
    i+=2
'''

name="shyrak"

for i in  range (0, len(name)-1, 2):
    print(name[i])