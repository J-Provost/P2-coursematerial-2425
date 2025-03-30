import re

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    @property
    def title(self):
        return self.__title

    @property
    def isbn(self):
        return self.__isbn

    @title.setter
    def title(self, value):
        if not value.strip(): 
            raise RuntimeError("Title cannot be empty")
        self.__title = value

    @isbn.setter
    def isbn(self, value):
        clean_isbn = re.sub(r"[\s-]", "", value)
        if not re.fullmatch(r"\d{13}", clean_isbn): 
            raise RuntimeError("Invalid ISBN format")

        digits = [int(d) for d in clean_isbn]

        checksum = sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits[:-1]))
        if (checksum + digits[-1]) % 10 != 0: 
            raise RuntimeError("Invalid ISBN checksum")

        self.__isbn = value