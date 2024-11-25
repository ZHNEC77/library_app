import unittest
from library import Library
from book import Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book(title="1984", author="Джордж Оруэлл", year="1949")
        self.book2 = Book(title="Убить пересмешника",
                          author="Харпер Ли", year="1960")
        self.library.books = [self.book1, self.book2]

    def test_add_book(self):
        initial_count = len(self.library.books)
        self.library.add_book()
        self.assertEqual(len(self.library.books), initial_count + 1)

    def test_delete_book(self):
        initial_count = len(self.library.books)
        self.library.delete_book()
        self.assertEqual(len(self.library.books), initial_count - 1)

    def test_find_book(self):
        found_books = self.library.find_book()
        self.assertIn(self.book1, found_books)
        self.assertIn(self.book2, found_books)

    def test_show_all_books(self):
        all_books = self.library.show_all_books()
        self.assertEqual(all_books, [self.book1, self.book2])

    def test_change_book_status(self):
        initial_status = self.book1.status
        self.library.change_book_status()
        self.assertNotEqual(self.book1.status, initial_status)


if __name__ == "__main__":
    unittest.main()
