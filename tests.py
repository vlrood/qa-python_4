from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_name_not_have_genre(self):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_add_new_book_with_empty_name_is_not_added(self):
        collector = BooksCollector()
        name = ''
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_should_be_added_(self, genre):
        collector = BooksCollector()
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_new_book_name_should_be_added(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict['name'])
        assert book_dict['name'] in collector.get_books_genre()

    def test_get_books_with_specific_genre_book_dict_get_list_of_books(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict['name'])
        collector.set_book_genre(book_dict['name'], book_dict['genre'])
        assert collector.get_books_with_specific_genre(book_dict['genre']) == [book_dict['name']]

    @pytest.mark.parametrize('genre_age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_genre_age_rating_not_added(self, genre_age_rating):
        collector = BooksCollector()
        name = 'Синистер'
        collector.add_new_book(name)
        collector.set_book_genre(name, genre_age_rating)
        assert collector.get_books_for_children() != genre_age_rating

    def test_add_book_in_favorites_book_dict_should_be_added(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict['name'])
        collector.set_book_genre(book_dict['name'], book_dict['genre'])
        collector.add_book_in_favorites(book_dict['name'])
        assert book_dict['name'] in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_dict_not_add_book_twice(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict['name'])
        collector.set_book_genre(book_dict['name'], book_dict['genre'])
        collector.add_book_in_favorites(book_dict['name'])
        collector.add_book_in_favorites(book_dict['name'])
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_dict_should_be_deleted(self, book_dict):
        collector = BooksCollector()
        collector.add_new_book(book_dict['name'])
        collector.set_book_genre(book_dict['name'], book_dict['genre'])
        collector.add_book_in_favorites(book_dict['name'])
        collector.delete_book_from_favorites(book_dict['name'])
        assert book_dict['name'] not in collector.get_list_of_favorites_books()
