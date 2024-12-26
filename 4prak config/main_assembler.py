import argparse
from assembler.assembler import assemble

def main():
    parser = argparse.ArgumentParser(description="Ассемблер для УВМ.")
    parser.add_argument("input_file", help="Входной файл с исходным кодом.")
    parser.add_argument("output_file", help="Выходной бинарный файл.")
    parser.add_argument("log_file", help="Файл лога в формате YAML.")
    args = parser.parse_args()

    assemble(args.input_file, args.output_file, args.log_file)

if name == "__main__":
    main()