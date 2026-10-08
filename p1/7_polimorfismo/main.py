#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import *

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul", "2020",180,150,6)
camion1= Camiones("Dina","Negro", "2020", 180, 300, 12, 8, 2500)
camion2= Camiones("Star", "Azul", "2019", 150, 200, 14, 6, 2000)
camioneta1= Camionetas("Renault", "Amarillo", "2025", 240, 250, 8, "delantera", True)
camioneta2= Camionetas("Nissan", "Blanca", "2020", 180, 150, 6, "trasera", False)


#---------------------------------------------------------------------------------------------
print(coche1.getVelocidad())

for i in range (1, 101):
    coche1.acelerar()

print(coche1.getVelocidad())


coche1.setVelocidad(400)
print(coche1.getVelocidad())
#----------------------------------------------------------------------------------------------
print("\nCamion 1:", camion1.getMarca(), camion1.getColor(), camion1.getModelo())
print("Velocidad inicial:", camion1.getVelocidad())
camion1.acelerar()
print("Velocidad tras acelerar:", camion1.getVelocidad())
camion1.frenar()
print("Velocidad tras frenar:", camion1.getVelocidad())
camion1.cargar("Material de construcción")
print("Capacidad de carga:", camion1.getCapacidadCarga())
camion1.setCapacidadCarga(3000)
print("Nueva capacidad de carga:", camion1.getCapacidadCarga())
print("Número de ejes:", camion1.getEje())
camion1.setEje(10)
print("Nuevo número de ejes:", camion1.getEje())

print("\n Camioneta 1:", camioneta1.getMarca(), camioneta1.getColor(), camioneta1.getModelo())
print("Velocidad inicial:", camioneta1.getVelocidad())
camioneta1.acelerar()
print("Velocidad tras acelerar:", camioneta1.getVelocidad())
camioneta1.frenar()
print("Velocidad tras frenar:", camioneta1.getVelocidad())
camioneta1.transportar(5)
print("Tracción:", camioneta1.getTraccion())
camioneta1.setTraccion("4x4")
print("Nueva tracción:", camioneta1.getTraccion())
print("¿Está cerrada?:", camioneta1.getCerrada())
camioneta1.setCerrada(False)
print("¿Está cerrada ahora?:", camioneta1.getCerrada())

#-----------------------------------------------------------------------------------------------


