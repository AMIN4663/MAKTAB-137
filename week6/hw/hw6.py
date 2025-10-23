"""
Library management system

"""
import pickle as pk
from datetime import datetime , timedelta

class Member:
    def __init__(self,name:str,number_id:int,email:str):
        self.name=name
        self.number_id=number_id
        self.email=email
        self.borrowed_books=[]
        self.broow_time = None
    
    def borrow_book(self,book:str):
        if book not in self.borrowed_books:
            self.broow_time=datetime.now()
            self.borrowed_books.append(book)
            return f"borrow book:{book}\t time:{self.broow_time}\treturn_time:{self.broow_time + timedelta(hours=2)}"
    
    def return_book(self,book:str):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return f"removed book:{book} "
        return f"not found book in list"
        
    def show_info(self):
        if self.borrowed_books!=[]:
            return f"number_id:{self.number_id}\nname:{self.name}\nemail:{self.email}\nbooks:\n{self.borrowed_books}"
        return f"number_id:{self.number_id}\nname:{self.name}\nemail:{self.email}\nbooks:"
        
user=Member("amin",9,"l")
print(user.borrow_book("python"))
class Book:
    total_book=0
    def __init__(self,title:str,author:str,isbn:int,is_borrowed=True):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.is_borrowed=is_borrowed
        Book.total_book+=1
    
        
    
    def mark_as_borrowed(self):
        if  not self.is_borrowed:
            self.is_borrowed=True
            print(f"Borrowed book")
    
    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed=False
            print(f"The loan book is returned")
    
    def display_info(self):
        print(f"title:{self.title}\nauthor:{self.author}\nisbn:{self.isbn}\nstatus:{self.is_borrowed}")


# book_1=Book("pyton","Eric",12345)
# book_1.display_info()

# book_1.mark_as_returned()
# book_1.display_info()
# book_1.mark_as_borrowed()
# book_1.display_info()

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]
    
    def add_book(self,book):
        for new_book in self.books:
            if new_book.isbn==book.isbn:
                print('error')
                return
        self.books.append(book)
        print(f"added book:{book.title}")
    
    def add_memberr(self,member):
        for new_member in self.members:
            if new_member.name==member.name:
                print('error')
                return
        self.members.append(member)
        print(f"added member:{member.name}")
    
    def borrow_Book(self,number_id:int,isbn:int):
        for book in self.books:
            if book.isbn==isbn:
                for m in self.members:
                    if m.number_id==number_id:
                        book.mark_as_borrowed()
                    else:
                        print(f"number id not found:{number_id}")
            else:
                print(f"not found isbn:{isbn}")
                
    def return_Book(self,number_id,isbn):
         for book in self.books:
            if book.isbn==isbn:
                for m in self.members:
                    if m.number_id==number_id:
                        book.mark_as_returned()
                    else:
                        print(f"number id not found:{number_id}")
            else:
                print(f"not found isbn:{isbn}")

    def show_all_book(self):
        print("________status___book___________")
        for book in self.books:
            print(f"book:{book.title}\tauthor:{book.author}\tisbn:{book.isbn}\tstatus:{book.is_borrowed}")

        
    def show_all_member(self):
        print('______status___member_____')
        for member in self.members:
            print(f"number_id:{member.number_id}\tname:{member.name}")

# new_user=Library("amin")
# b1=Book("python","eric",123)
# b2=Book("p","john",658)

# new_member1=Member("amin",1,"M")
# n_m2=Member("ali",2,"B")

# new_user.add_book(b1)
# new_user.add_book(b2)

# new_user.add_memberr(new_member1)
# new_user.add_memberr(n_m2)

# new_user.return_Book(1,123)
# new_user.borrow_Book(1,123)


# new_user.show_all_book()
# new_user.show_all_member()
class StudentMember(Member):
    
    def borrow_book(self,book:str):
        if book not in self.borrowed_books and len(self.borrowed_books)<3:
            self.borrowed_books.append(book)
            return f"added to list book:{book}"


class TeacherMember(Member):
     def borrow_book(self,book:str):
        if book not in self.borrowed_books and len(self.borrowed_books)<5:
            self.borrowed_books.append(book)
            return f"added to list book:{book}"
    


        