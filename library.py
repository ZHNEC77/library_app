import json
import os
from book import Book
from typing import List, Optional

DATA_FILE: str = "data.json"


class Library:
    def __init__(self):
        self.books: List[Book] = self.load_data()

    def load_data(self) -> List[Book]:
        """Загружает данные из файла."""
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data: List[dict] = json.load(f)
            return [Book(title=book['title'], author=book['author'], year=book['year'], status=book['status']) for book in data]
        except json.JSONDecodeError:
            print("Ошибка: Невозможно прочитать файл данных.")
            return []

    def save_data(self) -> None:
        """Сохраняет данные в файл."""
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([book.to_dict() for book in self.books],
                          f, indent=4, ensure_ascii=False)
        except IOError:
            print("Ошибка: Невозможно сохранить данные в файл.")

    def validate_input(self, field: str, message: str) -> str:
        """Проверяет, что поле не пустое."""
        value: str = input(message)
        if not value:
            raise ValueError(f"Поле {field} не может быть пустым.")
        return value

    def find_book_by_id(self, book_id: str) -> Optional[Book]:
        """Ищет книгу по id."""
        for book in self.books:
            if book.id == book_id:
                return book
        raise ValueError("Книга с таким id не найдена.")

    def add_book(self) -> None:
        """Добавляет книгу в библиотеку."""
        try:
            title: str = self.validate_input(
                "название", "Введите название книги: ")
            author: str = self.validate_input(
                "автора", "Введите автора книги: ")
            year: str = self.validate_input(
                "года издания", "Введите год издания книги: ")
            book: Book = Book(title=title, author=author, year=year)
            self.books.append(book)
            self.save_data()
            print("Книга успешно добавлена!")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def delete_book(self) -> None:
        """Удаляет книгу из библиотеки."""
        try:
            book_id: str = self.validate_input("id", "Введите id книги: ")
            book: Optional[Book] = self.find_book_by_id(book_id)
            if book:
                self.books.remove(book)
                self.save_data()
                print("Книга успешно удалена!")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def find_book(self) -> None:
        """Ищет книги по заданным критериям."""
        try:
            query: str = self.validate_input(
                "поиска", "Введите название, автора или год издания книги: ")
            found_books: List[Book] = [book for book in self.books if query.lower(
            ) in book.title.lower() or query.lower() in book.author.lower() or query == book.year]
            if found_books:
                print("Найденные книги:")
                for book in found_books:
                    print(book)
            else:
                print("Книги не найдены.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def show_all_books(self) -> None:
        """Отображает все книги в библиотеке."""
        if self.books:
            print("Список всех книг:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

    def change_book_status(self) -> None:
        """Изменяет статус книги."""
        try:
            book_id: str = self.validate_input("id", "Введите id книги: ")
            book: Optional[Book] = self.find_book_by_id(book_id)
            if book:
                new_status: str = self.validate_input(
                    "статуса", "Введите новый статус книги (в наличии/выдана): ")
                if new_status not in ["в наличии", "выдана"]:
                    raise ValueError("Неверный статус.")
                book.status = new_status
                self.save_data()
                print("Статус книги успешно изменен!")
        except ValueError as e:
            print(f"Ошибка: {e}")
