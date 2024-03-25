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

    def test_add_new_book_collector_book_not_have_genre(self, collector):
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert collector.get_book_genre(name) == ''

    def test_set_book_genre_collector_should_be_added(self, collector):
        collector.add_new_book('Гарфилд')
        collector.set_book_genre('Гарфилд', 'Комедии')
        assert collector.get_book_genre('Гарфилд') == 'Комедии'

    @pytest.mark.parametrize(
        'book_name',
        [
            "",
            "Звездные войны Эпоха Республики. Дарт Мол",
            "Звёздные войны. Эпоха Восстания. Боба Фетт",
            "Звездные войны Эпоха Восстания. Дарт Вейдер",
        ]
    )
    def test_add_new_book_collector_book_name_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    @pytest.mark.parametrize(
        'name',
        [
            'А',
            'Ра',
            'Звёздные войны: Дарт Бейн. Династия зла',
            'Звёздные войны: Старая Республика. Реван'
        ]
    )
    def test_add_new_book_collector_book_name_should_be_added(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_get_books_with_specific_genre_collector_get_list_of_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_for_children_collector_not_added(self, collector):
        collector.add_new_book('Синистер')
        collector.set_book_genre('Синистер', 'Ужасы')
        assert collector.get_books_for_children() != 'Ужасы'

    def test_add_book_in_favorites_collector_should_be_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_collector_not_add_book_twice(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_collector_should_be_deleted(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()
