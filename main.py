from app.io.input import input_text_from_console, read_file_builtin
from app.io.output import output_to_console, write_file_builtin
import os


def main():
    """
    Координує процес виконання програми:
    1. Зчитує текст з консолі
    2. Записує його у файл
    3. Зчитує дані з файлу різними способами
    4. Виводить результати в консоль
    """

    if not os.path.exists('data'):
        os.makedirs('data')

    user_input = input_text_from_console()

    output_to_console(f"Ви ввели: {user_input}")

    file_path = "data/results.txt"
    write_file_builtin(file_path, user_input)

    content = read_file_builtin(file_path)
    print(f"Зчитано з файлу: {content}")

if __name__ == "__main__":
    main()