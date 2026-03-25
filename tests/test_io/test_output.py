import unittest
import os
from app.io.output import write_file_builtin


class TestOutputFunctions(unittest.TestCase):
    """Клас для перевірки функцій запису у файл та виводу в консоль"""
    def test_write_file_builtin(self):
        test_path = "data/test_output.txt"
        test_data = "hello world"
        write_file_builtin(test_path, test_data)

        with open(test_path, "r") as f:
            self.assertEqual(f.read(), test_data)


if __name__ == '__main__':
    unittest.main()