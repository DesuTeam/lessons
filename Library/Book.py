class Book:
    def __init__(self, id: int, name: str, author: str, year: str):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return self.name + ' ' + str(self.id) + ' ' + self.author + ' ' + str(self.year)