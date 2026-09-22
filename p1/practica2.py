"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
## Se crea primero la clase, no hay objetos sin una clase previa
class Coches:
    def __init__(self, color, marca, velocidad):
        self.color=color #Encapsulamiento privado 2 guion bajo
        self.__marca=marca #Encapsulamiento privado 2 guion bajo
        self.__velocidad=velocidad #Encapsulamiento privado 2 guion bajo

    def acelerar(self):  
        self.__velocidad+=1

    def frenar(self):
        self.__velocidad-=1

    def tocar_claxon(self):
        print("PI PI PI")


#Instanciar o crear objetos de la clase Coches
coche1=Coches("Blanco","VW",220)
coche2=Coches("Azul","Nissan",180)

#print(f"El color del coche 1 es: {coche1.color}") No se pueden utilizar directamente los atributos porque son privados. No se usa

print(f"El claxón del coche 1 hace:")
coche1.tocar_claxon()
print(f"El claxón del coche 2 hace:")
coche2.tocar_claxon()
print(f"La aceleración del coche 1 es:")
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.acelerar()
coche1.frenar()




