import pytest
from main import BooksCollector
 # фикстура для пустого Collector
@pytest.fixture
def collector():
    return BooksCollector()

# фикстура с несколькими книгами и жанрами
@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    # добавляем книги разных жанров
    collector.add_new_book('Марсианин')       # фантастика
    collector.add_new_book('Мстители')               # фантастика
    collector.add_new_book('Закулисье реальности')                # ужасы
    collector.add_new_book('Поезд в Пусан')            # ужасы
    collector.add_new_book('Три кота')    # мультфильм
    collector.add_new_book('Финник')   # мультфильм
    collector.add_new_book('Сказочный патруль')        # мультфильм

    # устанавливаем жанры
    collector.set_book_genre('Марсианин', 'Фантастика')
    collector.set_book_genre('Мстители', 'Фантастика')
    collector.set_book_genre('Закулисье реальности', 'Ужасы')
    collector.set_book_genre('Поезд в Пусан', 'Ужасы')
    collector.set_book_genre('Три кота', 'Мультфильмы')
    collector.set_book_genre('Финник', 'Мультфильмы')
    collector.set_book_genre('Сказочный патруль', 'Мультфильмы')
    return collector