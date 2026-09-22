"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5,3))

#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulos:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base * self.altura

rect=Rectangulos(5,3)
print(rect.area())

##Nueva Forma
class Rectangulo:
    def area(self, base, altura):
        areaR=base*altura
        return areaR

rectangulo1=Rectangulos() #Crear o instaciar un objeto "rectangulo1" de la clase "Rectangulos"
print(f"El área del rectángulo es: {rectangulo1.area(5,6)}")