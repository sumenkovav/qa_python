# Тестовые данные
BOOKS_DATA = [
    {'name': 'Марсианин', 'genre': 'Фантастика'},
    {'name': 'Мстители', 'genre': 'Фантастика'},
    {'name': 'Закулисье реальности', 'genre': 'Ужасы'},
    {'name': 'Поезд в Пусан', 'genre': 'Ужасы'},
    {'name': 'Три кота', 'genre': 'Мультфильмы'},
    {'name': 'Финник', 'genre': 'Мультфильмы'},
    {'name': 'Сказочный патруль', 'genre': 'Мультфильмы'},
] 

FAVORITE_LIST_SCENARIOS = [
    {'input_name': 'A', 'expected_result': ['A']},           # Валидное, должно быть в списке
    {'input_name': 'B' * 40, 'expected_result': ['B' * 40]}, # Валидное, длинное
    {'input_name': '', 'expected_result': []},               # Невалидное, список пуст
    {'input_name': 'C' * 41, 'expected_result': []},         # Невалидное, список пуст
] 
