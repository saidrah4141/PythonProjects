'''
Created on Aug. 5, 2022

* Check and Print numbers divisible by 5

@author: Said
'''
'''
def div_Five(list):
    
    for x in range(len(list)):
        if list[x] % 5 == 0:
            print(list[x])
        
            
            
thisList = [10,20,23,34,50,60]
div_Five(thisList)           
'''

thisList = [10,20,23,34,50,60]

for x in thisList:
    if x % 5 == 0:
        print(x)