import argparse
from interpreter.interpreter import interpret

def main():
    parser = argparse.ArgumentParser(description="Интерпретатор для УВМ.")
    parser.add_argument("input_file", help="Входной бинарный файл.")
    parser.add_argument("output_file", help="Файл результата в формате YAML.")
    parser.add_argument("--memory_range", nargs=2, type=int, required=True, help="Диапазон памяти.")
    args = parser.parse_args()

    interpret(args.input_file, args.output_file, args.memory_range)

if name == "__main__":
    main()