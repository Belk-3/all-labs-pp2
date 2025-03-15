import string
import os

output_dir = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2"

for letter in string.ascii_uppercase:
    file_path = os.path.join(output_dir, f"{letter}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Файл {letter}.txt\n")

print("Файлы A-Z созданы.")
