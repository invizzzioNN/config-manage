import argparse
from config_parser.parser import parse_config
import toml

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(description="Парсер учебного конфигурационного языка в TOML.")
    parser.add_argument("input_file", type=argparse.FileType("r"), help="Входной файл с конфигурацией.")
    parser.add_argument("output_file", type=argparse.FileType("w"), help="Файл для сохранения результата в формате TOML.")
    args = parser.parse_args()

    # Чтение входного файла
    input_text = args.input_file.read()

    try:
        # Парсинг текста
        parsed_data = parse_config(input_text)
        # Запись результата в выходной файл
        toml.dump(parsed_data, args.output_file)
        print("Конфигурация успешно преобразована в формат TOML.")
    except Exception as e:
        print(f"Ошибка: {e}")

if name == "__main__":
    main()