import argparse
import sys

from toolkit.converter import convertation
from toolkit.errors import ToolkitErrors
from toolkit.pipeline import pipeline


def main() -> None:
    '''Обрабатывает аргументы командной строки и запускает нужную команду'''

    parser = argparse.ArgumentParser(prog='toolkit', description='...')

    subparsers = parser.add_subparsers(dest='command')

    calc_parser = subparsers.add_parser('calc', help='Вычислить выражение')
    calc_parser.add_argument('expr', help='Арифметическое выражение')

    convert_parser = subparsers.add_parser('convert', help='Конвертировать величину')
    convert_parser.add_argument('value', help='Начальное значение')
    convert_parser.add_argument('--from', dest='from_unit', required=True, help='Начальная единица')
    convert_parser.add_argument('--to', dest='to_unit', required=True, help='Конечная единица')

    args = parser.parse_args()

    try:
        if args.command == 'calc':
            print(pipeline(args.expr))
        elif args.command == 'convert':
            print(convertation(float(args.value), args.from_unit, args.to_unit))
    except ToolkitErrors as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
