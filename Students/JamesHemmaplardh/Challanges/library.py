
class library(object):
    def __init__(self, library_name):
        self.library_name = library_name  
        self.shelves = []    
        self.books = []      
    def library_collection(self):       
        print "The books in this library are:"
        for book in self.books:
            print book
    def book_count(self): 
        print "Number of Books in library:", len(self.books)
    def shelf_count(self):
        print "Number of shelves in library:", len(self.shelves)

class shelf(object):
    def __init__(self, shelf_name, library):
        self.shelf_name = shelf_name
        self.shelf_contents = []   
        library.shelves.append(self)
    def books_on_shelf(self):
        print "books in shelf %s:" % (self.shelf_name)
        for i in self.shelf_contents:
            print i 

class Book(object):
    def __init__(self, title, library):
        self.title = title
        library.books.append(self.title) 
    def enshelf(self, shelf_name):
        self.shelf_name = shelf_name
        self.shelf_name.shelf_contents.append(self.title)
    def unshelf(self, shelf_name):
        self.shelf_name = shelf_name
        self.shelf_name.shelf_contents.remove(self.title) 
        

james = library("The Library of James")
greetings = shelf('greetings', james)
goodbyes = shelf('goodbyes', james)
hi = Book('saying hi', james)
bye = Book('saying goodbye', james)
hi.enshelf(greetings)
bye.enshelf(goodbyes)

james.library_name
james.shelf_count()
james.book_count()
james.library_collection()
greetings.books_on_shelf()
goodbyes.books_on_shelf()

bye.unshelf(goodbyes)
goodbyes.books_on_shelf()
