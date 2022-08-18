'''
Created on Aug. 15, 2022

*1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

@author: Said
'''

class computation:
    def __init__ (self):
        pass
    def factorial(self,n):
        j = 1
        for i in range (1, n + 1):
            j = j * i
        print(j)
    def sum(self,n):
        j=0
        for i in range(1,n+1):
            j=j+i
        print(j)
    def testPrim(self,n):
        j = 0
        for i in range (1, n + 1):
            if (n% i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False

         
    def testPrims(self, n, m):
        x=0
        numPrim=0
        for y in range(n,m+1):
           if computation.testPrim(self, y):
               return True
               break
           else:
               return False
    def tableMult(self,n):
        for i in range(1,11):
            print(i*n)
    def allTablesSet(self):
        for i in range(1,11):
            for x in range(1,11):
                print(i*x,end=" ")
            print("\n")
    def listDiv(self,n):
        
        Ldiv=[]
        listDivPrime=[]
        for i in range(1,n+1): 
            
            if n% i == 0: 
                Ldiv.append(i)
            
            if n%i == 0 and self.testPrim(i) == False:
                listDivPrime.append(i)
        print(Ldiv[0:],"\n",listDivPrime[0:])
    
            
        
                
                
                
            

Comput= computation ()
Comput.listDiv(18)
