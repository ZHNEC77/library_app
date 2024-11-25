import unittest
from unittest.mock import patch
from library import Library
from book import Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()
        self.book1 = Book(
            title="1984", author="Джордж Оруэлл", year=1949)
        self.book2 = Book(title="Убить пересмешника",
                          author="Харпер Ли", year=1960)
        self.library.books = [self.book1, self.book2]

    def test_load_data(self):
        #  Проверяем, что данные загружаются корректно
        self.assertEqual(len(self.library.books), 2)
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)

    def test_save_data(self):
        # Проверяем, что данные сохраняются корректно
        self.library.save_data()

    @patch('builtins.input', return_value="Test")
    def test_validate_input(self, mock_input):
        # Проверяем, что валидация ввода работает корректно
        self.assertEqual(self.library.validate_input(
            "test", "Введите значение: "), "Test")

    @patch('builtins.input', return_value="")
    def test_validate_input_empty(self, mock_input):
        # Проверяем, что валидация ввода работает корректно с пустым значением
        with self.assertRaises(ValueError):
            self.library.validate_input(
                "test", "Введите значение: ")

    @patch('builtins.input', side_effect=['Новая книга', 'Новый автор', '2023'])
    def test_add_book(self, mock_input):
        # Проверяем, что книга успешно добавляется в библиотеку
        initial_count = len(self.library.books)
        self.library.add_book()
        self.assertEqual(len(self.library.books), initial_count + 1)

    # @patch('builtins.input', return_value="1984")
    # @patch('builtins.print')
    # def test_find_book(self, mock_print, mock_input):
    #     # Проверяем, что поиск книг работает корректно
    #     self.library.find_book()
    #     mock_print.assert_any_call(self.book1)
    #     mock_print.assert_any_call("Найденные книги:")
    #     mock_print.assert_not_called_with(self.book2)

    @patch('builtins.print')
    def test_show_all_books(self, mock_print):
        # Проверяем, что отображение всех книг работает корректно
        self.library.show_all_books()
        mock_print.assert_any_call(self.book1)
        mock_print.assert_any_call(self.book2)


if __name__ == "__main__":
    unittest.main()
