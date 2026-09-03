import pytest

from main import BooksCollector

from test_data import BOOKS_DATA

# Создаем список пар для тестирования. 
# Берем из наших общих данных.

BOOK_PAIRS = [
    (BOOKS_DATA[0]['name'], BOOKS_DATA[1]['name']),       # Пара 1: Книга 1 и Книга 2
    (BOOKS_DATA[0]['name'], BOOKS_DATA[-1]['name']),      # Пара 2: Первая и Последняя
    (BOOKS_DATA[2]['name'], BOOKS_DATA[3]['name']),       # Пара 3: Книги из середины
]


# проверка добавления новой книги
def test_add_new_book_add_one_book(collector):
    # проверяем, что книга добавилась и ёё жанр пустой
    book_name = BOOKS_DATA[0]['name']
    collector.add_new_book(book_name)
    assert book_name in collector.get_books_genre() 
    assert collector.get_book_genre(book_name) == ''    

# проверка установки жанра книге
def test_set_book_genre_correct(collector):
    # Берем имя книги из общих данных
    book_name = BOOKS_DATA[0]['name']
    target_genre = 'Фантастика'
    
    # Добавляем книгу (используем имя из данных)
    collector.add_new_book(book_name)
    
    # Устанавливаем жанр
    collector.set_book_genre(book_name, target_genre)
    
    # Проверяем результат
    assert collector.get_book_genre(book_name) == target_genre 


# проверка получения жанра книги по ее имени
def test_get_book_genre_returns_right_genre(collector_with_books):
    # Ищем книгу "Марсианин" в наших общих данных
    marsianin = next(book for book in BOOKS_DATA if book['name'] == 'Марсианин')
    # Ищем книгу "Закулисье реальности"
    zakulisie = next(book for book in BOOKS_DATA if book['name'] == 'Закулисье реальности')
    
    # Проверяем, используя данные из BOOKS_DATA
    assert collector_with_books.get_book_genre(marsianin['name']) == marsianin['genre']
    assert collector_with_books.get_book_genre(zakulisie['name']) == zakulisie['genre'] 


# проверка получения списка книг с определенным жанром
def test_get_books_with_specific_genre(collector_with_books):
    target_genre = 'Фантастика'
    
    # Считаем, сколько книг этого жанра должно быть согласно нашим данным
    expected_books_count = sum(1 for book in BOOKS_DATA if book['genre'] == target_genre)
    # Получаем список книг из коллектора
    books = collector_with_books.get_books_with_specific_genre(target_genre)
    
    # Проверяем количество
    assert len(books) == expected_books_count
    
    # Проверяем, что все ожидаемые книги действительно есть в результате
    for book in BOOKS_DATA:
        if book['genre'] == target_genre:
            assert book['name'] in books 


# проверка получения словаря
def test_get_books_genre_returns_dict(collector_with_books):
    books_dict = collector_with_books.get_books_genre()
    
    # Проверяем тип
    assert isinstance(books_dict, dict)
    
    # Проверяем, что количество книг совпадает с нашими данными
    assert len(books_dict) == len(BOOKS_DATA)
    
    # Проверяем, что каждая книга из наших данных есть в словаре
    for book in BOOKS_DATA:
        assert book['name'] in books_dict 


# проверка получения книг подходящих детям
def test_get_books_for_children_excludes_rated(collector_with_books):

    books_for_children = collector_with_books.get_books_for_children()
    
    # Находим все книги жанра "Ужасы и Детективы" в наших данных
    banned_genres = ['Ужасы', 'Детективы']
    books_that_must_not_be_here = [
        book['name'] 
        for book in BOOKS_DATA 
        if book['genre'] in banned_genres
    ]
    
    # Проверяем, что ни одна из запрещённых книг не попала в список
    for book_name in books_that_must_not_be_here:
        assert book_name not in books_for_children, \
            f"Книга '{book_name}' ({book['genre']}) не должна быть в списке детских, но она там есть!"
    
    # Cписок детских книг не должен быть пустым
    assert len(books_for_children) > 0, "Список детских книг не должен быть пустым" 


# проверка добавления книги в Избранное
def test_add_book_in_favorites_adds_book(collector):
    # Берем имя первой книги из наших общих данных
    book_name = BOOKS_DATA[0]['name']
    
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    
    # Проверяем, что в списке избранного именно эта книга
    assert collector.get_list_of_favorites_books() == [book_name] 


# проверка удаления книги из Избранного
def test_delete_book_from_favorites(collector):
    # Берем имя книги из общих данных
    book_name = BOOKS_DATA[0]['name']
    
    # Добавляем книгу в коллекцию
    collector.add_new_book(book_name)
    
    # Добавляем книгу в избранное
    collector.add_book_in_favorites(book_name)
    
    # Проверяем, что книга действительно есть в избранном ДО удаления
    assert book_name in collector.get_list_of_favorites_books()
    
    # Удаляем книгу из избранного
    collector.delete_book_from_favorites(book_name)
    
    # Проверяем, что книги больше нет в избранном ПОСЛЕ удаления
    assert book_name not in collector.get_list_of_favorites_books()
    assert collector.get_list_of_favorites_books() == [] 



# проверка получения списка всех Избранных книг
@pytest.mark.parametrize('book1_name, book2_name', BOOK_PAIRS)

def test_get_list_of_favorites_books_returns_correct_list(collector, book1_name, book2_name):
    # Добавляем книги в коллектор
    collector.add_new_book(book1_name)
    collector.add_new_book(book2_name)
    
    # Добавляем в избранное
    collector.add_book_in_favorites(book1_name)
    collector.add_book_in_favorites(book2_name)
    
    # Получаем список избранного
    favorites = collector.get_list_of_favorites_books()
    
    # Проверяем, что список совпадает с ожидаемым порядком добавления
    assert favorites == [book1_name, book2_name] 
