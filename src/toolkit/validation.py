from toolkit.constants import BINAR_OPERATORS, UNIVERSAL_OPERATORS
from toolkit.errors import (
    EmptyExpressionError,
    MissingOperator,
    TwoBinarOperator,
    UnknownSymbolError,
)


def validation(tokens: list[str]) -> None:
    '''Проверяет корректность выражения'''

    if not(tokens):
        raise EmptyExpressionError('Пустая строка')

    for token in tokens:
        if token not in BINAR_OPERATORS + UNIVERSAL_OPERATORS:
            try:
                float(token)
            except ValueError:
                raise UnknownSymbolError('Неизвестный символ')

    wait_num = True
    i = 0

    while i < len(tokens):
        if wait_num:
            if tokens[i] in UNIVERSAL_OPERATORS:
                i += 1
            else:
                try:
                    float(tokens[i])
                    wait_num = False
                    i += 1
                except ValueError:
                    if i == 0:
                        raise MissingOperator('Ожидалось число или унарный оператор') # хз как понять какую ошибку выдавать
                    if i > 0:
                        raise TwoBinarOperator('Два бинарных оператора подряд')
        else:
            if tokens[i] not in UNIVERSAL_OPERATORS + BINAR_OPERATORS:
                raise MissingOperator('Пропущен оператор')
            else:
                wait_num = True
                i += 1

    if wait_num:
        raise MissingOperator('Выражение не может заканчиваться оператором')
