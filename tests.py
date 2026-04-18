import pytest
from main import BooksCollector

class TestBooksCollector:

    # Пример теста
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 1. Тесты для add_new_book
    def test_add_new_book_normal_name(self):
        collector = BooksCollector()
        name = "Война и мир"
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        assert collector.get_book_genre(name) == ''

    def test_add_new_book_duplicate_name_not_added(self):
        collector = BooksCollector()
        name = "Дубровский"
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        long_name = "А" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize("name", ["Книга", "К" * 40])
    def test_add_new_book_boundary_names(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # 2. Тесты для set_book_genre
    def test_set_book_genre_valid_genre(self):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)
        collector.set_book_genre(name, "Фантастика")
        assert collector.get_book_genre(name) == "Фантастика"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)
        collector.set_book_genre(name, "Роман")
        assert collector.get_book_genre(name) == ""

    def test_set_book_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("Нет такой книги", "Фантастика")
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize("genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"])
    def test_set_book_genre_all_valid_genres(self, genre):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # 3. Тесты для get_book_genre
    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        name = "Книга"
        collector.add_new_book(name)
        collector.set_book_genre(name, "Ужасы")
        assert collector.get_book_genre(name) == "Ужасы"

    def test_get_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Нет такой книги") is None

    # 4. Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_have_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.set_book_genre("Книга2", "Детективы")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == ["Книга1"]

    def test_get_books_with_specific_genre_no_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Комедии")
        books = collector.get_books_with_specific_genre("Ужасы")
        assert books == []

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        books = collector.get_books_with_specific_genre("Нежанр")
        assert books == []

    # 5. Тесты для get_books_genre
    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        assert isinstance(collector.get_books_genre(), dict)

    # 6. Тесты для get_books_for_children
    def test_get_books_for_children_excludes_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book("Детская")
        collector.add_new_book("Ужасная")
        collector.set_book_genre("Детская", "Комедии")
        collector.set_book_genre("Ужасная", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Детская" in children_books
        assert "Ужасная" not in children_books

    def test_get_books_for_children_no_books(self):
        collector = BooksCollector()
        collector.add_new_book("Ужас")
        collector.set_book_genre("Ужас", "Ужасы")
        assert collector.get_books_for_children() == []

    # 7. Тесты для add_book_in_favorites
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert collector.get_list_of_favorites_books().count("Книга") == 1

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Нет книги")
        assert collector.get_list_of_favorites_books() == []

    # 8. Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.delete_book_from_favorites("Книга")
        assert collector.get_list_of_favorites_books() == []

    # 9. Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()
        assert isinstance(collector.get_list_of_favorites_books(), list)
        