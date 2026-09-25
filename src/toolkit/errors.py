class ToolkitErrors(Exception):
    '''Общий класс для ошибок пакета toolkit'''

class EmptyExpressionError(ToolkitErrors):
    '''Возникает при пустом выражении'''

class UnknownSymbolError(ToolkitErrors):
    '''Возникает при наличии неизвестного символа в выражении'''

class MissingOperator(ToolkitErrors):
    '''Возникает при отсутствии необходимого оператора'''

class TwoBinarOperator(ToolkitErrors):
    '''Возникает при наличии двух бинарных операторов подряд'''

class DivisionByZeroError(ToolkitErrors):
    '''Возникает при попытке деления на ноль'''

class UnknownUnitError(ToolkitErrors):
    '''Возникает при введении неизвестной единицы измерения'''

class IncompatibleUnitsError(ToolkitErrors):
    '''Возникает при попытке конвертации между несовместимыми единицами'''

class AbsoluteZeroError(ToolkitErrors):
    '''Возникает при значении температуры ниже абсолютного нуля'''
