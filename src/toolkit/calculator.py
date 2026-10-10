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

    res_expr: list[float | str] = list(merge_unary(expr))

    while '*' in res_expr or '/' in res_expr:
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
        res_expr = res_expr_1

    result = float(res_expr[0])
    j = 1

    while j < len(res_expr):
        if res_expr[j] == '+':
            result += float(res_expr[j+1])
            j += 2
        elif res_expr[j] == '-':
            result -= float(res_expr[j+1])
            j += 2

    return result
