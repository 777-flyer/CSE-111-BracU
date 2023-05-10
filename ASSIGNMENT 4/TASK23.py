class Author:

    def __init__(self, name=None):

        self.name = name
        self.book_list = {}

    def setName(self, new_name):

        self.name = new_name

    def addBook(self, book_name, book_genre):

        if self.name is None:
            print("A book name can not be added without author name.")

        else:
            if book_genre not in self.book_list:
                self.book_list[book_genre] = [book_name]
            else:
                self.book_list[book_genre].append(book_name)

    def printDetail(self):
        number = 0
        for length in self.book_list.values():
            number += (len(length))
        print(f'Number of Book(s): {number}')
        print(f"Author Name: {self.name}")

        for genre, books in self.book_list.items():
            print(genre + ":", ", ".join(books))

        print(self.book_list)
            

a1 = Author()
print("=================================")
a1.addBook('Ice', 'Science Fiction')
print("=================================")
a1.setName('Anna Kavan')
a1.addBook('Ice', 'Science Fiction')
a1.printDetail()
print("=================================")
a2 = Author('Humayun Ahmed')
a2.addBook('Onnobhubon', 'Science Fiction')
a2.addBook('Megher Upor Bari', 'Horror')
print("=================================")
a2.printDetail()
a2.addBook('Ireena', 'Science Fiction')
print("=================================")
a2.printDetail()
print("=================================")
