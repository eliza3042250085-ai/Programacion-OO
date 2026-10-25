from coches import coches

class App:
        def __init__(self):
            self.main()

        def borrarPantalla(self):
            print("\033c")

        def esperarTecla(self):
            input("... ¡Oprima cualquier tecla para continuar! ...")

        def menu_acciones(self, tipo):
            print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
            opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar\n\t 5.- Salir \n \t\tElige una Opcion: ").strip().lower()
            return opcion

        def respuesta_sql(self, respuesta):
            if respuesta:
                input("\n\t...¡Accion Realizada con Exito!...")
            else:
                input("\n\t...¡Esta Accion no pudo realizarse en este momento!...")

        def datos_coche(self, tipo):
            self.borrarPantalla()
            print(f"\n\t...ingresa los datos del {tipo}")
            cochesitos = {}
            cochesitos['marca'] = input("Ingrese la marca: ").strip()
            cochesitos['color'] = input("Ingrese el color: ").strip()
            cochesitos['modelo'] = input("Ingrese el modelo: ").strip()
            cochesitos['velocidad'] = int(input("Ingrese la velocidad: ").strip())
            cochesitos['potencia'] = int(input("Ingrese la potencia: ").strip())
            cochesitos['asientos'] = int(input("Ingrese el numero de asientos: ").strip())
            return cochesitos

        def menuCoche(self):
            opcion = True
            while opcion:
                self.borrarPantalla()
                opcion = self.menu_acciones("Coches")
                match opcion:
                    case "1":
                        #Crear objetos de la clase coches
                        #Utilizar la clase coches para crear un objeto, los valores del objeto se tienen que solicitar 
                        vehiculos = self.datos_coche("Coches")
                        coche = coches.Coches(vehiculos['marca'], vehiculos['color'], vehiculos['modelo'], vehiculos['velocidad'], vehiculos['potencia'], vehiculos['asientos'])
                        repuesta = coche.insertar()
                        self.respuesta_sql(repuesta)
                        del coche
                        
                    case "2":
                        self.borrarPantalla()
                        id = int(input("Ingresa el ID del coche a eliminar: ").strip())
                        respuesta = coches.Coches.eliminar(id)
                        self.respuesta_sql(respuesta)

                    case "3":
                        self.borrarPantalla()
                        id = int(input("Ingresa el ID del coche a actualizar: ").strip())
                        vehiculos = self.datos_coche("Coches")
                        coche = coches.Coches(vehiculos['marca'], vehiculos['color'], vehiculos['modelo'], vehiculos['velocidad'], vehiculos['potencia'], vehiculos['asientos'])
                        respuesta = coche.actualizar(id)
                        self.respuesta_sql(respuesta)
                        del coche
                        
                    case "4":
                        self.borrarPantalla()
                        registros = coches.Coches.consultar()
                        if len(registros) > 0:
                            num_coches = 1
                            for fila in registros:
                                print(f"Coche # {num_coches}\n\t ID: {fila[0]}\n\t Marca: {fila[1]}\n\t Color: {fila[2]}\n\t Modelo: {fila[3]}\n\t Velocidad: {fila[4]}\n\t Potencia: {fila[5]}\n\t Asientos: {fila[6]}")
                                num_coches += 1
                                self.esperarTecla()
                        else:
                            print("\n\n\t ¡No existen datos que mostrar por el momento!")
                            self.esperarTecla()

                    case "5":
                        opcion = False
                    case _:
                        self.borrarPantalla()
                        print("Opcion invalida, vuelve a intentarlo porfavor...")
                        self.esperarTecla()                       

        def main(self):
            opcion = True
            while opcion:
                self.borrarPantalla()
                opcion=input("\n\t 1.- Coches \n\t 2.- Salir\n \t\tElige una Opcion: ").strip().lower()
                match opcion:
                    case "1":
                        self.borrarPantalla()
                        self.menuCoche()
                        self.esperarTecla()

                    case "2":
                        self.borrarPantalla()
                        print("Salir del sistema...")
                        opcion = False

                    case _:
                        self.borrarPantalla()
                        print("Opcion invalida, vuelve a intentarlo porfavor...")
                        self.esperarTecla()



if __name__ == "__main__":
    app = App()