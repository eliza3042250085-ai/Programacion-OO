from conexionBD import *

class CochesBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.asientos = asientos

    def insertar(self):
        try: 
            cursor.execute("insert into coches VALUES (NULL , %s, %s, %s, %s, %s, %s)", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos))
            conexion.commit()
            return True
        except:
            return False

    def consultar(self):
        try:
            cursor.execute("select * from coches")
            return cursor.fetchall()
        except:
            return []

    def eliminar(self, id):
        try:
            cursor.execute("delete from coches where id = %s", (id,))
            conexion.commit()
            return True

        except:
            return False

    def actualizar(self, id):
        try:
            cursor.execute("update coches set marca = %s, color = %s, modelo = %s, velocidad = %s, potencia = %s, asientos = %s where id = %s", (self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.plazas, id))
            conexion.commit()
            return True
        except:
            return False