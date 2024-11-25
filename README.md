# Библиотека книг
Это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и отображать книги, а также изменять их статус.

# Функционал

# 1. Добавление книги
Пользователь вводит название, автора и год издания книги. Приложение генерирует уникальный идентификатор и добавляет книгу в библиотеку со статусом "в наличии".

Пример:
Введите название книги: 1984
Введите автора книги: Джордж Оруэлл
Введите год издания книги: 1949
Книга успешно добавлена!

# 2. Удаление книги
Пользователь вводит идентификатор книги, которую нужно удалить. Приложение удаляет книгу из библиотеки.

Пример:
Введите id книги: 1
Книга успешно удалена!

# 3. Поиск книги
Пользователь может искать книги по названию, автору или году издания. Приложение выводит список найденных книг.

Пример:
Введите название, автора или год издания книги: 1984
Найденные книги:
1. 1984, Джордж Оруэлл, 1949, в наличии

# 4. Отображение всех книг
Приложение выводит список всех книг с их идентификатором, названием, автором, годом издания и статусом.

Пример:
Список всех книг:
1. 1984, Джордж Оруэлл, 1949, в наличии
2. Убить пересмешника, Харпер Ли, 1960, выдана

# 5. Изменение статуса книги
Пользователь вводит идентификатор книги и новый статус ("в наличии" или "выдана"). Приложение изменяет статус книги.

Пример:
Введите id книги: 1
Введите новый статус книги (в наличии/выдана): выдана
Статус книги успешно изменен!

# Дополнительные требования
Хранение данных: Данные хранятся в формате JSON.

Обработка ошибок: Приложение корректно обрабатывает ошибки
Чистота и читаемость кода: Код аннотирован и документирован для улучшения читаемости.

Удобство использования интерфейса командной строки: Интерфейс командной строки простой и понятный.

Структура проекта: Проект разделен на три файла: main.py, library.py и book.py.
# Cтруктура проекта
library_app/
│
├── main.py
├── library.py
├── book.py
├── data.json
├── tests/
│   ├── __init__.py
│   └── test_library.py
├── README.md


# Использование
Клонируйте репозиторий:
git clone https://github.com/

1. Перейдите в директорию проекта:
cd library_app

2. Запустите приложение:
python main.py

# Пример использования
Добро пожаловать в библиотеку!

Выберите действие:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
6. Выход

Введите номер действия: 1

Введите название книги: 1984
Введите автора книги: Джордж Оруэлл
Введите год издания книги: 1949

Книга успешно добавлена!

Введите номер действия: 4

Список всех книг:
1. 1984, Джордж Оруэлл, 1949, в наличии

Введите номер действия: 6

До свидания!

# Тестирование
Для запуска тестов используйте следующую команду в корневой директории проекта:

python -m unittest discover tests


# Документация
load_data
Загружает данные из файла.

Аргументы:

None

Возвращает:

list[Book]: Список объектов Book.

save_data
Сохраняет данные в файл.

Аргументы:

None

Возвращает:

None

validate_input
Проверяет, что поле не пустое.

Аргументы:

field: str: Название поля.

message: str: Сообщение для пользователя.

Возвращает:

str: Введенное значение.

find_book_by_id
Ищет книгу по id.

Аргументы:

book_id: str: Идентификатор книги.

Возвращает:

Optional[Book]: Найденная книга или None, если книга не найдена.

add_book
Добавляет книгу в библиотеку.

Аргументы:

None

Возвращает:

None

delete_book
Удаляет книгу из библиотеки.

Аргументы:

None

Возвращает:

None

find_book
Ищет книги по заданным критериям.

Аргументы:

None

Возвращает:

None

show_all_books
Отображает все книги в библиотеке.

Аргументы:

None

Возвращает:

None

change_book_status
Изменяет статус книги.

Аргументы:

None

Возвращает:

None