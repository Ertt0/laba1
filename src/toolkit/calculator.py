from toolkit.constants import BINAR_OPERATORS, UNIVERSAL_OPERATORS
from toolkit.errors import DivisionByZeroError


def merge_unary(tokens:list[str]) -> list[str]:
    '''Объединяет последовательности унарных знаков с последующим числом.'''

    expr = []
    i = 0

    while i < len(tokens):
        if tokens[i] in UNIVERSAL_OPERATORS and (i == 0 or tokens[i-1] in BINAR_OPERATORS + UNIVERSAL_OPERATORS):
            count_minus = 0
            while i < len(tokens) and tokens[i] in UNIVERSAL_OPERATORS:
                if tokens[i] == '-':
                    count_minus += 1
                i += 1
            if count_minus % 2 == 0:
                expr.append(tokens[i])
            else:
                expr.append('-' + tokens[i])
            i += 1
        else:
            expr.append(tokens[i])
            i += 1

    return expr

def calculation(expr:list[str]) -> float:
    '''Вычисляет значение арифметического выражения'''

    expr = merge_unary(expr)
    res_expr = []

    if expr[0] in UNIVERSAL_OPERATORS:
        res_expr.append(expr[0]+expr[1])
        i = 2
    else:
        res_expr.append(expr[0])
        i = 1

    while i < len(expr):
        if expr[i] in UNIVERSAL_OPERATORS and expr[i-1] in UNIVERSAL_OPERATORS + BINAR_OPERATORS:
            res_expr.append(expr[i]+expr[i+1])
            i += 2
        else:
            res_expr.append(expr[i])
            i += 1

    j = 0
    res_expr_1: list[float | str] = []
    while j < len(res_expr):
        if res_expr[j] not in BINAR_OPERATORS + UNIVERSAL_OPERATORS:
            if j+1 < len(res_expr) and res_expr[j+1] == '*':
                res_expr_1.append(float(res_expr[j]) * float(res_expr[j+2]))
                j += 3
            elif j+1 < len(res_expr) and res_expr[j+1] == '/':
                if float(res_expr[j+2]) == 0:
                    raise DivisionByZeroError('Нельзя делить на ноль')
                res_expr_1.append(float(res_expr[j]) / float(res_expr[j+2]))
                j += 3
            else:
                res_expr_1.append(float(res_expr[j]))
                j += 1
        else:
            res_expr_1.append(res_expr[j])
            j += 1

    result = float(res_expr_1[0])
    j = 1

    while j < len(res_expr_1):
        if res_expr_1[j] == '+':
            result += float(res_expr_1[j+1])
            j += 2
        elif res_expr_1[j] == '-':
            result -= float(res_expr_1[j+1])
            j += 2

    return result
