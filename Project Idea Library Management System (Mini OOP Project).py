"""
Project Idea: Library Management System (Mini OOP Project)
Classes you might have:


Book with attributes: isbn, title, author, quantity
Library with attribute: a list of Book objects
Methods in Library:
add_book(book) — add book to library
remove_book(isbn) — remove book by ISBN
lend_book(isbn, user) — reduce quantity by 1, or error if none left
"""
class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
    # def __str__(self):
    #      return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) "

    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
       for b in self.books:
           if b.isbn == book.isbn:
               b.quantity += book.quatities
               return
       self.books.append(book)   

     
    def remove_book(self,isbn):
        for b in self.books:
            if b.isbn == isbn:
                self.books.remove(b)
                return True
        return False  
    

    def lend_book(self, isbn, user):
        for b in self.books:
            if b.isbn == isbn:
                if b.quantity > 0:
                    b.quantity -= 1
                    return f"Book '{b.title}' lent to {user}"
                else:
                    return "Book out of stock"

        return "Book not found"


page = Book(isbn="6254278", title="codeing book", author="yazi", quantity=7)
lib = Library()
print(page.isbn)
print(page.title)
print(page.author)
print(page.quantity)
lib.add_book(page)
print(lib.lend_book("6254278", "Alice"))
lib.remove_book('6254278')

         

    



        




