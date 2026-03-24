import pandas as pd

def input_text_from_console():
    return input("Введіть текст: ")
    """
    Зчитує текст, введений користувачем безпосередньо в консоль
    Повертає: рядок (str) з введеним текстом
    """

def read_file_builtin(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    """
    Зчитує вміст файлу
    Аргументи: file_path (str) - шлях до файлу
    Повертає: рядок (str) з вмістом файлу
    """
def read_file_pandas(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()
    """
    Зчитує вміст файлу
    Аргументи: file_path (str) - шлях до файлу
    Повертає: вміст у вигляді рядка або об'єкта DataFrame
    """