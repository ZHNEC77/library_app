from library import Library


def main() -> None:
    """Главная функция приложения."""
    library: Library = Library()
    while True:
        print("\nДобро пожаловать в библиотеку!")
        print("Выберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice: str = input("Введите номер действия: ")
        try:
            if choice == "1":
                library.add_book()
            elif choice == "2":
                library.delete_book()
            elif choice == "3":
                library.find_book()
            elif choice == "4":
                library.show_all_books()
            elif choice == "5":
                library.change_book_status()
            elif choice == "6":
                print("До свидания!")
                break
            else:
                raise ValueError("Неверный выбор. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
