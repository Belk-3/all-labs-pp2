import psycopg2

def insert_or_update_user(username, userphone, useroperator):
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(
            dbname="mydatabase",
            user="postgres",
            password="Magnat_kaef_Bekzhan",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Вызов процедуры вставки или обновления пользователя
        cursor.execute(
            "CALL insert_or_update_user_by_name_and_phone(%s, %s, %s);",
            (username, userphone, useroperator)
        )
        
        # Подтверждаем изменения
        connection.commit()
        
        print(f"Пользователь '{username}' успешно добавлен или обновлен.")
    
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection:
            connection.close()

# Пример использования:
if __name__ == "__main__":
    # Запрашиваем у пользователя данные для вставки или обновления
    name = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")
    operator = input("Введите оператора: ")

    insert_or_update_user(name, phone, operator)
