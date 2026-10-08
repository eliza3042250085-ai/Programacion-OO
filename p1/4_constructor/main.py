#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches

coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul", "2020",180,150,6)

coche1.acelerar()
coche2.acelerar()