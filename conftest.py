import pytest
from main import BooksCollector
# Импортируем данные из нашего отдельного файла
from test_data import BOOKS_DATA

# фикстура для пустого Collector
@pytest.fixture
def collector():
    return BooksCollector()

# фикстура с несколькими книгами и жанрами
@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    
    # добавляем все книги
    for book in BOOKS_DATA:
        collector.add_new_book(book['name'])
    
    # устанавливаем жанры
    for book in BOOKS_DATA:
        collector.set_book_genre(book['name'], book['genre'])
        
    return collector 