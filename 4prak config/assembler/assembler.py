import yaml
import struct

# Константы для типов команд
INSTRUCTION_FORMATS = {
    30: {"size": 5, "format": "BBBBB"},  # Загрузка константы
    8: {"size": 5, "format": "BBBBB"},   # Чтение из памяти
    11: {"size": 5, "format": "BBBBB"},  # Запись в память
    39: {"size": 5, "format": "BBBBB"},  # popcnt()
}

def parse_instruction(line):
    """Парсинг строки инструкции в байтовый формат."""
    parts = line.split()
    opcode = int(parts[0])
    args = [int(x) for x in parts[1:]]

    if opcode not in INSTRUCTION_FORMATS:
        raise ValueError(f"Неизвестная команда: {opcode}")

    fmt = INSTRUCTION_FORMATS[opcode]["format"]
    return struct.pack(fmt, opcode, *args)

def assemble(input_file, output_file, log_file):
    """Ассемблирование программы."""
    with open(input_file, "r") as f:
        lines = f.readlines()

    binary_data = []
    log_data = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):  # Пропуск комментариев
            continue

        instruction = parse_instruction(line)
        binary_data.append(instruction)
        log_data.append({"instruction": line, "bytes": list(instruction)})

    # Запись бинарного файла
    with open(output_file, "wb") as f:
        f.write(b"".join(binary_data))

    # Запись лога
    with open(log_file, "w") as f:
        yaml.dump(log_data, f, default_flow_style=False)