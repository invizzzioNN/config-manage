import re
from config_parser.evaluator import evaluate_expression

COMMENT_REGEX = r"--.*"
CONSTANT_DEF_REGEX = r"(\w+)\s*->\s*(\w+);"
EXPR_REGEX = r"\^\[([\w\s+\-*\/mod().]+)\]"
NUMBER_REGEX = r"^\d+$"
NAME_REGEX = r"^[A-Z]+$"
DICT_REGEX = r"\{(.*?)\}"

constants = {}

def parse_config(input_text):
    """Парсер учебного конфигурационного языка"""
    global constants
    constants = {}
    input_text = re.sub(COMMENT_REGEX, "", input_text).strip()
    lines = input_text.splitlines()

    result = {}
    for line in lines:
        line = line.strip()

        # Пропуск пустых строк
        if not line:
            continue

        # Объявление константы
        if match := re.match(CONSTANT_DEF_REGEX, line):
            value, name = match.groups()
            if re.match(NUMBER_REGEX, value):
                constants[name] = int(value)
            else:
                raise ValueError(f"Неверное значение константы: {line}")

        # Константное выражение
        elif match := re.match(EXPR_REGEX, line):
            expr = match.group(1)
            constants["_result"] = evaluate_expression(expr, constants)

        # Словари
        elif match := re.match(DICT_REGEX, line):
            dict_content = match.group(1)
            dict_items = [item.strip() for item in dict_content.split(",") if item.strip()]
            parsed_dict = {}
            for item in dict_items:
                if "=" not in item:
                    raise ValueError(f"Неверный элемент словаря: {item}")
                key, value = map(str.strip, item.split("="))
                if not re.match(NAME_REGEX, key):
                    raise ValueError(f"Неверное имя: {key}")
                if re.match(NUMBER_REGEX, value):
                    parsed_dict[key] = int(value)
                elif value in constants:
                    parsed_dict[key] = constants[value]
                else:
                    raise ValueError(f"Неверное значение: {value}")
            result.update(parsed_dict)

        else:
            raise ValueError(f"Неизвестная строка: {line}")

    return result