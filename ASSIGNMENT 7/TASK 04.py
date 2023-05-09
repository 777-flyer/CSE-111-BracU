class Product:

    def __init__(self, _id, title, price):
        self.__id = _id
        self.__title = title
        self.__price = price

    def get_id_title_price(self):
        return "ID: " + str(self.__id) + " Title: " + self.__title + " Price: " + str(self.__price)


class Book(Product):

    def __init__(self, _id, title, price, isbn, publisher):
        super().__init__(_id, title, price)
        self.__isbn = isbn
        self.__publisher = publisher

    def printDetail(self):
        return self.get_id_title_price() + "\nISBN: " + self.__isbn + " Publisher: " + self.__publisher


class CD(Product):

    def __init__(self, _id, title, price, band, duration, genre):
        super().__init__(_id, title, price)
        self.__band = band
        self.__duration = duration
        self.__genre = genre

    def printDetail(self):
        return self.get_id_title_price() + "\nBand: " + self.__band + " Duration: " + str(
            self.__duration) + " minutes" + "\nGenre: " + self.__genre


book = Book(1, "The Alchemist", 500, "97806", "HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2, "Shotto", 300, "Warfaze", 50, "Hard Rock")
print(cd.printDetail())
