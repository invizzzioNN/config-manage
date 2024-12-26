import yaml
import struct

MEMORY_SIZE = 1024  # Размер памяти УВМ
REGISTER_COUNT = 16  # Количество регистров

class VirtualMachine:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.registers = [0] * REGISTER_COUNT

    def load_constant(self, reg, value):
        self.registers[reg] = value

    def read_memory(self, reg, addr):
        self.registers[reg] = self.memory[addr]

    def write_memory(self, reg, addr):
        self.memory[addr] = self.registers[reg]

    def popcnt(self, reg, addr, offset):
        address = self.registers[addr] + offset
        value = self.memory[address]
        self.registers[reg] = bin(value).count("1")

    def execute(self, instructions):
        for instr in instructions:
            opcode = instr[0]
            if opcode == 30:  # Загрузка константы
                _, reg, value = instr
                self.load_constant(reg, value)
            elif opcode == 8:  # Чтение из памяти
                _, reg, addr = instr
                self.read_memory(reg, addr)
            elif opcode == 11:  # Запись в память
                _, reg, addr = instr
                self.write_memory(reg, addr)
            elif opcode == 39:  # popcnt
                _, reg, addr, offset = instr
                self.popcnt(reg, addr, offset)

def interpret(input_file, output_file, memory_range):
    with open(input_file, "rb") as f:
        binary_data = f.read()

    instructions = [binary_data[i:i+5] for i in range(0, len(binary_data), 5)]
    instructions = [struct.unpack("BBBBB", instr) for instr in instructions]

    vm = VirtualMachine()
    vm.execute(instructions)

    # Сохранение результата в YAML
    result = {"memory": vm.memory[memory_range[0]:memory_range[1]]}
    with open(output_file, "w") as f:
        yaml.dump(result, f, default_flow_style=False)