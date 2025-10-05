class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []      
        self.members = []    
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.members.append(member)
    
    def lend_book(self, member_id, isbn):
       
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.isbn == isbn and b.is_available), None)
        
        if member and book:
            member.borrowed_books.append(book)
            book.is_available = False
            print(f"{book.title} lent to {member.name}")


library = Library("City Library")
book1 = Book("Python Programming", "John Smith", "123456")
member1 = Member("Alice", "M001")

library.add_book(book1)
library.register_member(member1)
library.lend_book("M001", "123456")