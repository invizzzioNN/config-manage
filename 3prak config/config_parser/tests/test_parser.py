import unittest
from config_parser.parser import parse_config

class TestConfigParser(unittest.TestCase):
    def test_constant_definition(self):
        input_text = "10 -> A;"
        parse_config(input_text)
        self.assertEqual(constants["A"], 10)

    def test_dictionary_parsing(self):
        input_text = "{ A = 10, B = 20 }"
        result = parse_config(input_text)
        self.assertEqual(result, {"A": 10, "B": 20})

    def test_expression_parsing(self):
        input_text = "10 -> A;\n^[A + 5]"
        result = parse_config(input_text)
        self.assertEqual(constants["_result"], 15)

    def test_invalid_syntax(self):
        input_text = "{ INVALID = 10"
        with self.assertRaises(ValueError):
            parse_config(input_text)

if name == "__main__":
    unittest.main()