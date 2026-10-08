"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion _init_(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self, velocidad):
        self._velocidad = velocidad

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getPotencia(self):
        return self._potencia
    
    def setPotencia(self, potencia):
        self._potencia = potencia

    def getAsientos(self):
        return self._asientos
    
    def setAsientos(self, asientos):
        self._asientos = asientos


class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, capacidadCarga, eje):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self._capacidadCarga = capacidadCarga
        self._eje = eje
            
    def cargar(self, tipo_carga):
        print(f"El tipo de carga es: {tipo_carga}")

    def acelerar(self):
        self.setVelocidad(self.getVelocidad() + 1)
        print("Estoy acelerando como un camión")

    def frenar(self):
        self.setVelocidad(self.getVelocidad() - 1)
        print("Estoy frenando como un camión")

    def setEje(self, eje):
        self.__eje = eje

    def getEje(self):
        return self.__eje

    def setCapacidadCarga(self, capacidadCarga):
        self.__capacidadCarga = capacidadCarga

    def getCapacidadCarga(self):
        return self.__capacidadCarga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__traccion = traccion
        self.__cerrada = cerrada

    def transportar(self, num_pasajeros):
        print(f"El número de pasajeros es: {num_pasajeros}")

    def acelerar(self):
        self.setVelocidad(self.getVelocidad() + 1)
        print("Estoy acelerando como una camioneta")

    def frenar(self):
        self.setVelocidad(self.getVelocidad() - 1)
        print("Estoy frenando como una camioneta")

    def setTraccion(self, traccion):
        self.__traccion = traccion

    def getTraccion(self):
        return self.__traccion

    def setCerrada(self, cerrada):
        self.__cerrada = cerrada

    def getCerrada(self):
        return self.__cerrada

    
    



coche1=Coches("VW","Blanco","2022",220,150,5)
coche2=Coches("Nissan","Azul", "2020",180,150,6)
        
