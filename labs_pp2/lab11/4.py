import psycopg2

try:
    connection = psycopg2.connect(
        dbname="mydatabase",
        user="postgres",
        password="Magnat_kaef_Bekzhan",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    # Первый запрос
    cursor.execute("SELECT * FROM get_users_with_pagination(5, 0);")
    rows1 = cursor.fetchall()
    print("Page 1:")
    for row in rows1:
        print(row)

    # Второй запрос
    cursor.execute("SELECT * FROM get_users_with_pagination(5, 5);")
    rows2 = cursor.fetchall()
    print("\nPage 2:")
    for row in rows2:
        print(row)

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection:
        connection.close()
