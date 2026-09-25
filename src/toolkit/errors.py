class ToolkitErrors(Exception):
    pass
class EmptyExpressionError(ToolkitErrors):
    pass
class UnknownSymbolError(ToolkitErrors):
    pass
class MissingOperator(ToolkitErrors):
    pass
class TwoBinarOperator(ToolkitErrors):
    pass
class DivisionByZeroError(ToolkitErrors):
    pass
class UnknownUnitError(ToolkitErrors):
    pass
class IncompatibleUnitsError(ToolkitErrors):
    pass
class AbsoluteZeroError(ToolkitErrors):
    pass
