def tokenization(expr: str) -> list[str]:
    '''Разбивает арифметическое выражение на токены'''
    current = ''
    tokens = []

    for symbol in expr:
        if symbol.isdigit() or symbol == '.':
            current += symbol
        elif symbol == ' ':
            if current:
                tokens.append(current)
            current = ''
        else:
            if current:
                tokens.append(current)
            current = ''
            tokens.append(symbol)

    if current:
        tokens.append(current)

    return tokens
