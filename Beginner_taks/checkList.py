'''
Created on Aug. 5, 2022

*check if first and last number of a list are the same

@author: Said
'''

def check_List (list):
    if list[0] == list[-1]:
        print("result is True")
    else:
        print("result is False")
        
list_1 = [10,20,30,40,10]
list_2 = [10,20,40,40,50]
check_List(list_1)
check_List(list_2)
        