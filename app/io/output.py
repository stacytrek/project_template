def output_to_console(text):
    print(text)
    """
    Виводить переданий текст у консоль користувача
    """

def write_file_builtin(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data)
    """
    Записує дані у файл
    Аргументи: file_path - куди писати, data - що писати
    """