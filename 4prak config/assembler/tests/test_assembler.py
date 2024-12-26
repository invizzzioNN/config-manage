import unittest
from assembler.assembler import parse_instruction

class TestAssembler(unittest.TestCase):
    def test_load_constant(self):
        instruction = parse_instruction("30 1 846")
        self.assertEqual(list(instruction), [0x5E, 0x3B, 0x0D, 0x00, 0x00])

    def test_read_memory(self):
        instruction = parse_instruction("8 6 239")
        self.assertEqual(list(instruction), [0x88, 0xBD, 0x03, 0x00, 0x00])

    def test_write_memory(self):
        instruction = parse_instruction("11 10 12")
        self.assertEqual(list(instruction), [0x8B, 0x32, 0x00, 0x00, 0x00])

    def test_popcnt(self):
        instruction = parse_instruction("39 6 2 217")
        self.assertEqual(list(instruction), [0xA7, 0x49, 0x36, 0x00, 0x00])

if name == "__main__":
    unittest.main()