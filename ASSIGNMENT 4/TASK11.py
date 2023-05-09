class Author:

    def __init__(self, name="Default", *books):

        self.name = name
        self.book_list = list(books)

    def addBooks(self, *book_name):

        self.book_list += list(book_name)

    def changeName(self, new_name):

        self.name = new_name

    def printDetails(self):

        print(f"Author Name: {self.name}")
        print("--------")
        print("List of Books:")
        for i in self.book_list:
            print(i, end="\n")


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()
