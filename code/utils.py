import json


def open_json_file():
    """Функция для открытия файла json"""
    with open('operations.json', 'r', encoding='utf=8') as file:
        files = file.read()
        content = json.loads(files)
        return content

