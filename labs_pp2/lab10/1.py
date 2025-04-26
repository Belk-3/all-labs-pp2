import psycopg2
import csv

def insert_from_csv(cursor, csv_filename):
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            cursor.execute("""
            INSERT INTO Phones (name, phone, operator)
            VALUES (%s, %s, %s);
            """, (row[0], row[1], row[2]))
    print("✔️ Data from CSV inserted successfully!")

try:
    # Connect to your PostgreSQL database тут кароче я подключаюсь к базе данных
    connection = psycopg2.connect(
        dbname="mydatabase",
        user="postgres",
        password="Magnat_kaef_Bekzhan",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

   
    insert_from_csv(cursor, 'file_csv.csv')  # Вставляем данные из CSV файла
    print(" Data inserted successfully!")

    
    # а здесь зоканчивается магия
    connection.commit()
except Exception as e:
    print(f"Error: {e}")
finally:
    #close the curs and connection
    if cursor:
        cursor.close()

    if connection:
        connection.close()

        