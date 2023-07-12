from random import choice

answers = [
    'Скорее да',
    'Скорее нет',
    'Возможно',
    'Не исключаю',
    'Вряд ли',
    'Точно нет',
    'На это есть все шансы'
]


def generate_answer():
    return choice(answers)