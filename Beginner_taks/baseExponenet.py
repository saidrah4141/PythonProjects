'''
Created on Aug. 8, 2022

@author: Said
'''



def exponent(base,exp):
    i=0
    ans=1
    while i <exp:
        ans= ans*base
        i+=1
    print(ans)

exponent(6, 2)
    