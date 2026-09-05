import pytest

from main import BooksCollector

from test_data import BOOKS_DATA

from test_data import FAVORITE_LIST_SCENARIOS

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
    
    # В наших данных 2 книги этого жанра.
    # Это и есть наш "ожидаемый результат".
    expected_books_count = 2 
    
    books = collector_with_books.get_books_with_specific_genre(target_genre)
    
    # Проверяем количество
    assert len(books) == expected_books_count
    
    # Проверяем наличие конкретных книг
    assert 'Марсианин' in books
    assert 'Мстители' in books 


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
    book_name = BOOKS_DATA[0]['name']
    
    # Подготовка: книга должна быть в избранном, чтобы её можно было удалить
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    
    # Удаляем книгу
    collector.delete_book_from_favorites(book_name)
    
    # Проверка: книги нет
    assert book_name not in collector.get_list_of_favorites_books()
    assert collector.get_list_of_favorites_books() == [] 



# проверка получения списка всех Избранных книг
@pytest.mark.parametrize('scenario', FAVORITE_LIST_SCENARIOS)
def test_get_list_of_favorites_books_returns_correct_list(collector, scenario):
    
    # Проверяет, что метод get_list_of_favorites_books() возвращает 
    # корректный список в зависимости от валидности имени книги.
    
    book_name = scenario['input_name']
    expected_list = scenario['expected_result']

    # Пытаемся добавить книгу в избранное
    # (Метод add_new_book сам проверит длину имени внутри себя)
    collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)

    # Получаем список избранного
    favorites = collector.get_list_of_favorites_books()

    # Сравниваем полученный список с ожидаемым
    assert favorites == expected_list
