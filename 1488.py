import os

def search_files_with_hash_symbol(directory='.'):
    # Получаем абсолютный путь текущей директории
    directory = os.path.abspath(directory)

    # Создаем список для хранения найденных файлов
    found_files = []

    # Проходим по всем подпапкам и файлам в текущей директории и ее подпапках
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверяем, содержится ли символ "#" в названии файла
            if '#' in file:
                # Если да, добавляем путь к файлу в список найденных файлов
                found_files.append(os.path.join(root, file))

    return found_files

if __name__ == "__main__":
    # Вызываем функцию с параметром текущей директории
    found_files = search_files_with_hash_symbol()

    # Выводим найденные файлы
    if found_files:
        print("Найдены файлы с символом '#' в названии:")
        for file in found_files:
            print(file)
    else:
        print("Файлы с символом '#' в названии не найдены.")
