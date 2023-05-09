class Library:

    def __init__(self, name, books):
        self.name = name
        self.books = books
        self.borrowers = {}

    def details(self):
        print(f"{self.name} Library details")
        print("Borrower details:")
        print(self.borrowers)
        print('Books availability:')
        print(self.books)


class Reader:

    def __init__(self, name):

        self.name = name
        self.readers_books = {}
        self.book_count = 0

    def borrow(self, location, *books):

        for book in books:

            if self.book_count < 5:

                if location.books[book] == 0:

                    print(f"{book} books are not available at this moment.")

                else:

                    location.books[book] = location.books[book] - 1

                    print(f"{book} is borrowed successfully!")

                    self.book_count += 1

                    location.borrowers[self.name] = self.book_count

                    if book not in self.readers_books:

                        self.readers_books[book] = 1

                    else:

                        self.readers_books[book] = self.readers_books[book] + 1

            else:

                print("You cannot borrow more than 5 books")

    def readerInfo(self, genre=None):

        if genre is not None:

            print(f"{self.name}, you have {self.readers_books[genre]} {genre} book(s) with you")

        else:

            print(f"{self.name}, you have {self.book_count} book(s) with you")

            for i in self.readers_books:
                
                print(f"Books on {i}: {self.readers_books[i]}")


L1 = Library('Dhaka', {'Arts': 15, 'Fiction': 135, 'Politics': 2, 'Science': 11, 'Poetry': 15})
L1.details()
print("1----------------------")
r1 = Reader('Aladdin')
r1.borrow(L1, 'Arts', 'Fiction', 'Fiction', 'Politics')
print("2----------------------")
r1.borrow(L1, 'Politics', 'Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2 = Reader('Jasmine')
r2.borrow(L1, 'Politics', 'Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
