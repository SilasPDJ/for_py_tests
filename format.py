class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def __format__(self, format_spec):
        formats = {
            "time": f'{self.pages / 60:.2f}h',
            "caps": self.title.upper()
        }

        return formats.get(format_spec, "")


if __name__ == "__main__":
    book1: Book = Book('Provérbios', 500)
    book2: Book = Book("Tito", 5)

    print(f"{book1:caps}")
    print(f"{book1:time}")
