# Тестирование класса BooksCollector

Проект содержит набор unit-тестов для класса `BooksCollector` с использованием `pytest`.  
Тесты покрывают все методы класса: добавление книг, установку жанра, фильтрацию, избранное и т.д.

## Список реализованных тестов

### Метод `add_new_book`
- `test_add_new_book_add_two_books` – добавление двух книг, проверка количества.
- `test_add_new_book_normal_name` – добавление книги с обычным названием.
- `test_add_new_book_duplicate_name_not_added` – повторное добавление той же книги не создаёт дубликат.
- `test_add_new_book_name_too_long` – название длиннее 40 символов не добавляется.
- `test_add_new_book_empty_name_not_added` – пустое название не добавляется.
- `test_add_new_book_boundary_names` – параметризованный тест для граничных значений (1 и 40 символов).

### Метод `set_book_genre`
- `test_set_book_genre_valid_genre` – установка допустимого жанра.
- `test_set_book_genre_invalid_genre` – установка недопустимого жанра не работает.
- `test_set_book_genre_for_nonexistent_book` – установка жанра для несуществующей книги.
- `test_set_book_genre_all_valid_genres` – параметризованная проверка всех доступных жанров.

### Метод `get_book_genre`
- `test_get_book_genre_existing_book` – получение жанра существующей книги.
- `test_get_book_genre_nonexistent_book` – получение жанра для отсутствующей книги (возвращает `None`).

### Метод `get_books_with_specific_genre`
- `test_get_books_with_specific_genre_have_books` – фильтрация книг по жанру.
- `test_get_books_with_specific_genre_no_books` – если книг с жанром нет, возвращается пустой список.
- `test_get_books_with_specific_genre_invalid_genre` – неверный жанр → пустой список.

### Метод `get_books_genre`
- `test_get_books_genre_returns_dict` – проверка, что возвращается словарь.

### Метод `get_books_for_children`
- `test_get_books_for_children_excludes_age_rating` – книги с возрастным рейтингом не попадают в детский список.
- `test_get_books_for_children_no_books` – если подходящих книг нет, возвращается пустой список.

### Метод `add_book_in_favorites`
- `test_add_book_in_favorites_success` – добавление книги в избранное.
- `test_add_book_in_favorites_duplicate_not_added` – повторное добавление не создаёт дубликат.
- `test_add_book_in_favorites_nonexistent_book` – добавление несуществующей книги не меняет список.

### Метод `delete_book_from_favorites`
- `test_delete_book_from_favorites_success` – удаление книги из избранного.
- `test_delete_book_from_favorites_not_in_favorites` – удаление отсутствующей книги не вызывает ошибок.

### Метод `get_list_of_favorites_books`
- `test_get_list_of_favorites_books_returns_list` – возвращается список (даже пустой).
