def copy_file(src, dst):
    try:
        with open(src, "r", encoding="utf-8") as source, open(dst, "w", encoding="utf-8") as destination:
            destination.write(source.read())
        print(f"Файл скопирован в {dst}")
    except FileNotFoundError:
        print("Исходный файл не найден")

source_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt"
copy_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG_copy.txt"

copy_file(source_path, copy_path)
