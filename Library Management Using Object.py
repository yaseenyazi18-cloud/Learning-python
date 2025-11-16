"""
5. Library Management Using Objects
Create a class Book with attributes: title, author, year, isbn.
Create a class Library which has:
An attribute books (a list)
Methods:
add_book(book_obj) — adds Book to library
remove_book(isbn) — removes the book with matching ISBN
search_by_title(title) — returns list of matching books (partial match allowed)
display_books() — prints all books in library with details
In main:
Create some Book objects, add them to Library
Demonstrate removing, searching, and showing all books


"""
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
   
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}"
        

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_obj):
        self.books.append(book_obj)
        print(f"Book added: {book_obj.title}")   
      
          

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
               self.books.remove(book)
               print(f"Book Removed: {book}")
               return 
        print("Book with given ISBN not found.")   
              
    def search_by_title(self, title):
        results = [ ]
        for book in self.books:
            if title.lower() in book.title.lower():
              results.append(book)
        return results
        


    def display_books(self):
        if not self.books:
            print("Library Empty.")
            return
       
        print("Library Books:")
        for book in self.books:
            print(book) 
    

library = Library()
# Create Book objects
book1 = Book("A Brief History of Time", "Stephen Hawking", 1988, "54321") 
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "67890")
book3 = Book("The Alchemist", "Paulo Coelho", 1988, "12345") 

  
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("\n-All Books in Library-------------------\n")
library.display_books()

print("\nSearching the title---------------------\n")
results = library.search_by_title("Th")
for book in results:
    print(book)

print("\nRemoving book with ISBIN------------------")
library.remove_book("12345")
print("\n")
library.display_books()
 












                   
               
               
            




    



        