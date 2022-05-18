# # TODO: Classes are defined using the class keyword

#     def __init__(self, title, author,
# class Book: price):
#         self._title= title
#         self._author= author
#         self._price= price

#     @property
#     def title(self):
#         return self._title

#     @title.setter
#     def title(self, value):
#          self._title= value

# # TODO: create an instance of the class
# b1 = Book("war And Peace", "Leo Tolstoy", 20,95)
# print(b1.title)
# b1.title = "Anna Karenia"
# print(b1.title)

# TODO: Classes are defined using the class keyword

class Book:
    def __init__(self, title, author, price):
          self._title= title
          self._author= author
          self._price= price

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        self._title= value

# TODO: create an instance of the class

b1 = Book("War and Peace", "Leo Tolstoy", 21.95)
print(b1.title)
b1.title = "Anna Karenina"
print(b1.title)