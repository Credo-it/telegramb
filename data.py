import json
DICT_DATA = 'data/quiz_data.json'
quiz_data = [
    {
        'question': 'Что такое Python?',
        'options': ['Язык программирования', 'Тип данных', 'Музыкальный инструмент', 'Змея на английском'],
        'correct_option': 0
    },
    {
        'question': 'Какой тип данных используется для хранения целых чисел?',
        'options': ['int', 'float', 'str', 'natural'],
        'correct_option': 0
    },
    {
        'question': 'Что такое PEP в мире Python?',
        'options': ['Python Enhancement Proposal', 'Python Error Protocol', 'Python Execution Plan', 'Python Extension Program'],
        'correct_option': 0
    },
    {
        'question': 'Как создать пустой список в Python?',
        'options': ['list()', '[]', '{}', 'set()'],
        'correct_option': 1
    },
    {
        'question': 'Чем отличается `list` от `tuple` в Python?',
        'options': ['Список изменяем, кортеж - нет', 'Кортеж изменяем, список - нет', 'Список и кортеж неотличимы', 'Список и кортеж неявляются типами данных в Python'],
        'correct_option': 0
    },
    {
        'question': 'Что такое `__init__` в классах Python?',
        'options': ['Стандартный метод инициализации класса', 'Конструктор', 'Деструктор', 'Метод, преобразующий класс в строку'],
        'correct_option': 1
    },
    {
        'question': 'Что такое lambda-функция в Python?',
        'options': ['Анонимная функция', 'Метод для создания переменных', 'Список переменных из модуля math', 'Функция для работы с вложенными данными'],
        'correct_option': 0
    },
    {
        'question': 'Какой оператор используется для проверки истинности двух значений в Python?',
        'options': ['is', '==', '!=', 'and'],
        'correct_option': 1
    },
    {
        'question': 'Что произойдет, если в Python выполнить операцию деления на ноль?',
        'options': ['Ошибка "ZeroDivisionError"', 'Получим значение `infinity`', 'Получим значение `NaN`', 'Ничего плохого не произойдет'],
        'correct_option': 0
    },
    {
        'question': 'Что такое генератор в Python?',
        'options': ['Функция, возвращающая значение', 'Структура данных', 'Объект, сохраняющий текущее состояние', 'Метод для создания исключений'],
        'correct_option': 2
    },
]

with open(DICT_DATA, 'w') as file:
    json.dump(quiz_data, file)