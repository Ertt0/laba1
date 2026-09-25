import pytest

from toolkit.calculator import calculation
from toolkit.converter import convertation
from toolkit.errors import (
    AbsoluteZeroError,
    DivisionByZeroError,
    EmptyExpressionError,
    IncompatibleUnitsError,
    MissingOperator,
    UnknownSymbolError,
    UnknownUnitError,
)
from toolkit.tokenization import tokenization
from toolkit.validation import validation


def test_tokenization_simple() -> None:
    assert tokenization('2+3') == ['2', '+', '3']

def test_tokenization_float() -> None:
    assert tokenization('2.5*4') == ['2.5', '*', '4']

def test_tokenization_space() -> None:
    assert tokenization(' 2 + 3 ') == ['2', '+', '3']

def test_tokenization_more_unar() -> None:
    assert tokenization('2 + - -- 3') == ['2', '+', '-', '-', '-', '3']

def test_tokenization_unary_op() -> None:
    assert tokenization('-5+3') == ['-', '5', '+', '3']

def test_tokenization_unkown() -> None:
    assert tokenization('2#3') == ['2', '#', '3']

def test_tokenization_space1() -> None:
    assert tokenization('2 3') == ['2', '3']


def test_validation_valid() -> None:
    validation(['2', '+', '1'])

def test_validation_empty_expression() -> None:
    with pytest.raises(EmptyExpressionError):
        validation([])

def test_validation_unknown_symbol() -> None:
    with pytest.raises(UnknownSymbolError):
        validation(['2', '+', '1.1.1'])

def test_validation_missing_operator_start() -> None:
    with pytest.raises(MissingOperator):
        validation(['*', '-', '+', '6'])

def test_validation_missing_operator_end() -> None:
    with pytest.raises(MissingOperator):
        validation(['6', '*', '-', '+'])

def test_validation_missing_operator() -> None:
    with pytest.raises(MissingOperator):
        validation(['6', '3'])

def test_validation_valid_unar() -> None:
    validation(['6', '*', '-', '+', '6'])



def test_convertation_valid_length() -> None:
    assert convertation(5, 'km', 'm') == 5000.0

def test_convertation_valid_length_caps() -> None:
    assert convertation(5, 'KM', 'M')

def test_convertation_valid_mass() -> None:
    assert convertation(5, 'g', 'kg') == 0.005

def test_convertation_different_groups() -> None:
    with pytest.raises(IncompatibleUnitsError):
        convertation(5, 'km', 'g')

def test_convertation_unknown_units() -> None:
    with pytest.raises(UnknownUnitError):
        convertation(5, 'kl', 'g')

def test_convertation_absolute_zero() -> None:
    with pytest.raises(AbsoluteZeroError):
        convertation(-2, 'k', 'c')

def test_convertation_valid_temp() -> None:
    assert convertation(290.15, 'k', 'c') == 17.0

def test_calculation_division_by_zero() -> None:
    with pytest.raises(DivisionByZeroError):
        calculation(['6', '/', '0'])

def test_calculation_valid() -> None:
    assert calculation(['2', '-', '-', '12']) == 14.0

def test_calculation_valid_double_unary_1() -> None:
    assert calculation(['6', '*', '-', '-', '6']) == 36.0

def test_calculation_valid_double_unary_2() -> None:
    assert calculation(['6', '-', '-', '+', '6']) == 12.0
