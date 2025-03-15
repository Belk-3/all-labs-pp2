import os

file_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt"

def check_access(path):
    print(f"Проверяем файл: {path}")
    print("Существует:", os.path.exists(path))
    print("Читаемый:", os.access(path, os.R_OK))
    print("Записываемый:", os.access(path, os.W_OK))
    print("Исполняемый:", os.access(path, os.X_OK))

check_access(file_path)
