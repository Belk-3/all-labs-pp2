def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print("Файл не найден")
        return 0

# Укажите путь
file_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt"
print("Количество строк в GG.txt:", count_lines(file_path))
