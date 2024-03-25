# qa_python 4 
Юнит-тестирование:
test_add_new_book_add_two_books - исправлен ассерт. Проверяет проверку на добавление названия двум книгам.
test_add_new_book_collector_book_not_have_genre - проверяется метод add_new_book_name, который по умолчанию добавляет 
исключительно название книгам. Провелась проверка на то, что у добавленной книги нет жанра
test_set_book_genre_collector_should_be_added - проверяется метод set_book_genre, который по умолчанию добавлет книге жанр.
Позитивная проверка на то, что жанр действительно добавлен.
test_add_new_book_collector_book_name_not_added - проверяет метод add_new_book_name, который добавлет книге название, которое 
может содержать максимум 40 символов. Проверка на длину названия книги. Используется техника анализа 
граничных значений.
test_add_new_book_collector_book_name_should_be_added - проверяет метод add_new_book_name, который добавлет книге название, которое 
может содержать максимум 40 символов. Позитивная проверка на длину символов названия книги.
test_get_books_with_specific_genre_collector_get_list_of_books - проверяет метод get_books_with_specific_genre, 
выводящий список книг с определенным жанром. Позитивная проверка, что метод возвращает список книг с опред. жанром.
test_get_books_for_children_collector_not_added - проверяет метод get_books_for_children, который возвращает 
книги, подходящие детям. Проверка на то, что метод не добавляет книги с возрастным рейтингом.
test_add_book_in_favorites_collector_should_be_added - проверяет метод add_book_in_favorites, который добавляет книгу 
в избранное. Провелась проверка на то, что книга добавляется в избранное.
test_add_book_in_favorites_collector_not_add_book_twice - проверяет метод add_book_in_favorites, который не может 
добавить одну и ту же книгу в избранное дважды. Позитивная проверка исключающая повтороное добавление.
test_delete_book_from_favorites_collector_should_be_deleted - проверяет метод delete_book_from_favorites, удаляющий 
книгу из избранного. Проверка на то, что книга удалится из избранного, если она там есть.
Также проверены методы get_book_genre (выводит жанр книги по ее имени), get_books_genre (выводит текущий словарь 
books_genre), get_list_of_favorites_books (получает список избранных книг)

Применена параметризация и фикстуры.
