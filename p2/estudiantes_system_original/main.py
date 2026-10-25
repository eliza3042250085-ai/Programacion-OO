from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main

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

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t...ingresa los datos del {tipo}")
        estudiantitos = {}
        estudiantitos['nombre'] = input("Ingrese el nombre: ").strip()
        estudiantitos['nota'] = float(input("Ingrese la nota: ").strip())
        return estudiantitos

    def menuEstudiante(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            match opcion:
                case "1":
                    estudiantitos = self.datos_estudiante("Estudiantes")
                    estudiante = estudiantes.Estudiantes(estudiantitos['nombre'], estudiantitos['nota'])
                    estudiante = estudiantes.Estudiantes(estudiante.getNombre(), estudiante.getNota())
                    respuesta = estudiante.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante

                case "2":
                    self.borrarPantalla()
                    estudiante = estudiantes.Estudiantes('', 0)
                    id = int(input("Ingresa el ID del estudiante a eliminar: ").strip())
                    respuesta = estudiante.eliminar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante

                case "3":
                    self.borrarPantalla()
                    id = int(input("Ingresa el ID del estudiante a modificar: ").strip())
                    respuesta = estudiantes.Estudiantes(id)
                    nombre = input("Ingresa el nuevo nombre: ").strip()
                    nota = input("Ingresa la nueva nota: ").strip()
                    self.respuesta_sql(respuesta)
                    del estudiante

                case "4":
                    self.borrarPantalla()
                    estudiante = estudiantes.EstudiantesBD('', 0)
                    registros = estudiante.consultar()
                    if len(registros) > 0:
                        num_estudiantes = 1
                        for fila in registros:
                            print(f"Coche # {num_estudiantes}\n\t ID: {fila[0]}\n\t Nombre: {fila[1]}\n\t Nota: {fila[2]}")
                            num_estudiantes += 1
                            self.esperarTecla()
                    else:
                        print("\n\n\t ¡No existen datos que mostrar por el momento!")
                    del coche

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
            opcion=input("\n\t 1.- Estudiantes \n\t 2.- Salir\n \t\tElige una Opcion: ").strip().lower()
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