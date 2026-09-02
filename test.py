import pytest

from main import BooksCollector



# проверка добавления новой книги
def test_add_new_book_add_one_book(collector):
    collector.add_new_book('Интерстеллар')
    # проверяем, что книга добавилась
    assert 'Интерстеллар' in collector.get_books_genre()
    # проверяем, что жанр пустой
    assert collector.get_book_genre('Интерстеллар') == ''

# проверка установки жанра книге
def test_set_book_genre_correct(collector):
    collector.add_new_book('Интерстеллар')
    collector.set_book_genre('Интерстеллар', 'Фантастика')
    assert collector.get_book_genre('Интерстеллар') == 'Фантастика'


# проверка получения жанра книги по ее имени
def test_get_book_genre_returns_right_genre(collector_with_books):
    assert collector_with_books.get_book_genre('Марсианин') == 'Фантастика'
    assert collector_with_books.get_book_genre('Закулисье реальности') == 'Ужасы'


# проверка получения списка книг с определенным жанром
def test_get_books_with_specific_genre(collector_with_books):
    books = collector_with_books.get_books_with_specific_genre('Фантастика')
    assert 'Марсианин' in books
    assert 'Мстители' in books
    assert len(books) == 2


# проверка получения словаря
def test_get_books_genre_returns_dict(collector_with_books):
    books_dict = collector_with_books.get_books_genre()
    assert 'Марсианин' in books_dict
    assert isinstance(books_dict, dict)


# проверка получения книг подходящих детям
def test_get_books_for_children_excludes_rated(collector_with_books):
    books_for_children = collector_with_books.get_books_for_children()
    # книги без возрастного рейтинга должны быть
    assert 'Три кота' in books_for_children
    assert 'Финник' in books_for_children
    assert 'Сказочный патруль' in books_for_children
    # книг с возрастным рейтингом не должно быть
    assert 'Закулисье реальности' not in books_for_children
    assert 'Поезд в Пусан' not in books_for_children


# проверка добавления книги в Избранное
def test_add_book_in_favorites_adds_book(collector):
    collector.add_new_book('Интерстеллар')
    collector.add_book_in_favorites('Интерстеллар')
    assert collector.get_list_of_favorites_books() == ['Интерстеллар']


# проверка удаления книги из Избранного
def test_delete_book_from_favorites(collector):
    # создаём книгу
    collector.add_new_book('Интерстеллар')

    # добавляем книгу в Избранное
    collector.add_book_in_favorites('Интерстеллар')
    # проверяем, что книга в избранном
    assert collector.get_list_of_favorites_books() == ['Интерстеллар']

    # удаляем из Избранного
    collector.delete_book_from_favorites('Интерстеллар')
    # проверяем, что её больше нет
    assert collector.get_list_of_favorites_books() == []


# проверка получения списка всех Избранных книг
def test_get_list_of_favorites_books_returns_correct_list(collector):
    collector.add_new_book('Интерстеллар')
    collector.add_new_book('Мстители')
    collector.add_book_in_favorites('Интерстеллар')
    collector.add_book_in_favorites('Мстители')
    favorites = collector.get_list_of_favorites_books()
    assert favorites == ['Интерстеллар', 'Мстители']
