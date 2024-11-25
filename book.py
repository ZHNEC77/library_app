import uuid
from typing import Dict


class Book:
    """Класс, представляющий книгу."""

    def __init__(self, title: str, author: str, year: str, status: str = "в наличии"):
        """Инициализирует объект книги."""
        self.id: str = str(uuid.uuid4())  # Генерируем уникальный идентификатор
        self.title: str = title
        self.author: str = author
        self.year: str = year
        self.status: str = status

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f"{self.id}. {self.title}, {self.author}, {self.year}, {self.status}"

    def to_dict(self) -> Dict[str, str]:
        """Возвращает словарь с данными книги."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }
