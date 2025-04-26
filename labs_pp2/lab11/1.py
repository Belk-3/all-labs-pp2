import psycopg2

def search_users_by_pattern(pattern):
    try:
        # Подключение к базе
        connection = psycopg2.connect(
            dbname="mydatabase",
            user="postgres",
            password="Magnat_kaef_Bekzhan",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Выполнение функции поиска
        cursor.execute("SELECT * FROM search_users_by_pattern(%s);", (pattern,))
        rows = cursor.fetchall()

        # Вывод результатов
        if rows:
            print(f"Найдено записей по шаблону '{pattern}':")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}, Operator: {row[3]}")
        else:
            print(f"По шаблону '{pattern}' ничего не найдено.")

    except Exception as e:
        print(f"Ошибка: {e}")
    
    finally:
        # Закрытие соединения
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

# Пример вызова функции
if __name__ == "__main__":
    pattern = input("Введите часть имени/номера/оператора для поиска: ")
    search_users_by_pattern(pattern)
