import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'README.md')           # добавляем к этому пути имя файла

print(file_path)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
