import psycopg2
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

   
    cursor.execute(" CALL delete_user(%s, %s)", ('Bekzhan', None) )  
   
   

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

        