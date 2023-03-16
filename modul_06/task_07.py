"""Розробіть функцію sanitize_file(source, output), що переписує у текстовий
файл output вміст текстового файлу source, очищений від цифр."""


def sanitize_file(source: str, output: str):
    """sanitize file"""
    with open(source, 'r') as file_data:
        line_data = ''.join(line for line in file_data)
        line_clean_data = ''.join(symbol for symbol in line_data if symbol not in '0123456789')

    with open(output, 'w') as file_output:
        file_output.write(line_clean_data)


sanitize_file('modul_06//task_06.txt', 'modul_06//task_07_out.txt')
