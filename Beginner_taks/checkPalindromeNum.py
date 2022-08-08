'''
Created on Aug. 6, 2022

*checks if a number is the same reverse ex. 545

@author: Said
'''

'''
def check_Palindrome(x):
    

    if int(str(x)[::-1]) == x:
        print("True")
    else:
        print("False")

check_Palindrome(545)
check_Palindrome(423)
'''
n = 543
reversed = 0
    
while(n!=0):
    r=int(n%10) ''' ----> type cast to int '''
    reversed = reversed*10 + r
    n=int(n/10)
print(reversed)