import os

def check_path(path):
    if os.path.exists(path):
        print(f"Путь существует: {path}")
        print("Файл:", os.path.basename(path))
        print("Директория:", os.path.dirname(path))
    else:
        print("Путь не существует")

# Укажите путь
check_path(r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt")
