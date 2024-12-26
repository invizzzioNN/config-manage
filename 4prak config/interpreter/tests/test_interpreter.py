import unittest
from interpreter.interpreter import VirtualMachine

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.vm = VirtualMachine()

    def test_load_constant(self):
        self.vm.load_constant(1, 846)
        self.assertEqual(self.vm.registers[1], 846)

    def test_read_memory(self):
        self.vm.memory[239] = 123
        self.vm.read_memory(6, 239)
        self.assertEqual(self.vm.registers[6], 123)

    def test_write_memory(self):
        self.vm.registers[10] = 456
        self.vm.write_memory(10, 100)
        self.assertEqual(self.vm.memory[100], 456)

    def test_popcnt(self):
        self.vm.memory[12] = 0b110101
        self.vm.registers[2] = 12
        self.vm.popcnt(6, 2, 0)
        self.assertEqual(self.vm.registers[6], 4)  # Количество единиц в 0b110101

if name == "__main__":
    unittest.main()