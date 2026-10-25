import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_estudiantes"
    )
    cursor = conexion.cursor(buffered=True)

except:
    print("...!Por el Momento no se puede conectarse con la base de datos, intente más tarde...!")
