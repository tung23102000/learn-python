class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

# shelf = BookShelf(300)

# print(shelf)

class Book:
    def __init__(self, name):
     
        self.name= name
    def __str__(self):
        return f"Book {self.name}"
book = Book("HP")
book2 = Book("HP2")
shelf=BookShelf(book,book2)
print(shelf)
print(shelf.books)