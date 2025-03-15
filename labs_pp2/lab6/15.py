def write_list_to_file(filename, data_list):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(str(item) + "\n")

data = ["Hello", "This is", "GG.txt file"]
file_path = r"C:\Users\User2025\OneDrive - АО Казахстанско-Британский Технический Университет\Документы\agh\all-labs-pp2\labs_pp2\GG.txt"

write_list_to_file(file_path, data)
print("Данные записаны в GG.txt")
