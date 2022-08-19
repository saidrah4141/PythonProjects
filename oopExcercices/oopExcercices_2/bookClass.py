'''
Created on Aug. 17, 2022

1 - Define a Book class with the following attributes: Title, Author (Full name), Price.
2 - Define a constructor used to initialize the attributes of the method with values entered by the user.
3 - Set the View() method to display information for the current book.
4 - Write a program to testing the Book class.

@author: Said
'''
class Book():
    def __init__(self,Title, Author, Price):
        self.title = Title
        self.author= Author
        self.price = Price
    def view(self):
        return(self.title,self.author,self.price)
        
book1 = Book("Harry Potter, " , "J.K Rowling, " , 15 )

print(book1.view())