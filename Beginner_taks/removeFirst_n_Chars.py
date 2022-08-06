'''
Created on Aug. 5, 2022

* removes first 2 , 3 ,4 ... chars of a string

@author: Said
'''

def remove_char(String , num):
    
    if num<len(String):
        print(String[num:])
        
    else:
        print("error")
    
remove_char("Train",3)