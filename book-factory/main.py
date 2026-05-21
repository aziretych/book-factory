import random


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


def generate_random_book():
    titles = [
        "The Lost World",
        "Python Basics",
        "Dark Ocean",
        "Future City",
        "Silent Night",
    ]

    authors = [""
        "John Smith",
        "Alice Brown",
        "Michael Lee",
        "Emma Wilson",
        "David Clark"
    ]

    year = random.randint(1899, 2026)

    return Book(random.choice(titles), random.choice(authors), year)


book = generate_random_book()
print(book)
