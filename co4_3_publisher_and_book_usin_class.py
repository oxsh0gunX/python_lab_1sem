class Publisher:
    def __init__(self, name):
        print("publisher class activated")
        self.name = name
    def display(self):
        print(f"Publisher Name : {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        print("Book Class is activated")
        self.title = title
        self.author = author
    def display(self):
        super().display()
        print(f"Title : {self.title}")
        print(f"author : {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, no_pages):
        super().__init__(name, title ,author)
        print("Python class activated")
        self.price = price
        self.no_pages = no_pages
    def display(self):
        super().display()
        print(f"Price : {self.price}")
        print(f"No_Pages : {self.no_pages}")

book1 = Python("DC", "Aadujeevitham", "Basheer", 540, 250)
book1.display()
