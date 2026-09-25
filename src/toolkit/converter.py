from toolkit.constants import LENGTH_UNITS, MASS_UNITS, TEMP_UNITS
from toolkit.errors import AbsoluteZeroError, IncompatibleUnitsError, UnknownUnitError


def to_kelvin(value, unit):
    '''Переводит температуру из указанной шкалы в Кельвины'''

    if unit == 'c':
        return value + 273.15
    elif unit == 'k':
        return value
    elif unit == 'f':
        return (value - 32) * 5/9 + 273.15


def from_kelvin(value_in_kelvin, unit):
    '''Переводит температуру из Кельвинов в указанную величину'''

    if value_in_kelvin < 0:
        raise AbsoluteZeroError('Температура не может быть ниже абсолютного нуля')
    if unit == 'c':
        return value_in_kelvin - 273.15
    elif unit == 'k':
        return value_in_kelvin
    elif unit == 'f':
        return (value_in_kelvin - 273.15) / (5/9) + 32

def convertation(value: float, from_unit: str, to_unit: str) -> float:
    '''Конвертирует величину из одной единицы измерения в другую'''

    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    if from_unit in TEMP_UNITS and to_unit in TEMP_UNITS:
        return from_kelvin(to_kelvin(value, from_unit), to_unit)
    elif from_unit not in LENGTH_UNITS and from_unit not in MASS_UNITS and from_unit not in TEMP_UNITS or\
    to_unit not in LENGTH_UNITS and to_unit not in MASS_UNITS and to_unit not in TEMP_UNITS:
        raise UnknownUnitError('Неизвестная единица измерения')

    elif from_unit in LENGTH_UNITS and to_unit in LENGTH_UNITS:
        result = float(value) * LENGTH_UNITS[from_unit] / LENGTH_UNITS[to_unit]
    elif from_unit in MASS_UNITS and to_unit in MASS_UNITS:
        result = float(value) * MASS_UNITS[from_unit] / MASS_UNITS[to_unit]
    else:
        raise IncompatibleUnitsError('Несовместимые единицы')

    return result
