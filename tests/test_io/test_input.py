import unittest
import os
from app.io.input import read_file_builtin

class TestInputFunctions(unittest.TestCase):
    """Клас, що містить набір тестів для перевірки коректності зчитування даних"""

    def setUp(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        with open("data/test_input.txt", "w") as f:
            f.write("test content")

    def test_read_file_builtin(self):
        """Перевіряє, чи функція read_file_builtin правильно повертає текст з файлу"""
        result = read_file_builtin("data/test_input.txt")
        self.assertEqual(result, "test content")

    def test_file_not_found(self):
        """Перевіряє виклик винятку FileNotFoundError при відсутності файлу"""
        with self.assertRaises(FileNotFoundError):
            read_file_builtin("data/non_existent.txt")

if __name__ == '__main__':
    unittest.main()