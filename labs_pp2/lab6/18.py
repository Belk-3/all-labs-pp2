import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Файл {path} удалён")
        else:
            print(f"Нет прав на удаление {path}")
    else:
        print("Файл не существует")

file_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt"
delete_file(file_path)
