import unittest
from config_parser.evaluator import evaluate_expression

class TestEvaluator(unittest.TestCase):
    def test_addition(self):
        result = evaluate_expression("10 + 5", {})
        self.assertEqual(result, 15)

    def test_mod_function(self):
        result = evaluate_expression("mod(10, 3)", {})
        self.assertEqual(result, 1)

    def test_with_constants(self):
        constants = {"A": 10, "B": 20}
        result = evaluate_expression("A + B", constants)
        self.assertEqual(result, 30)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            evaluate_expression("INVALID_EXPR", {})

if name == "__main__":
    unittest.main()