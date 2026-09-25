from toolkit.calculator import calculation
from toolkit.tokenization import tokenization
from toolkit.validation import validation


def pipeline(expr: str) -> float:
    '''Обрабатывает арифметическое выражение в правильной последовательности'''

    tokens = tokenization(expr)
    validation(tokens)
    return calculation(tokens)
