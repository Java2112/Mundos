class Mundos:
    def __init__(self):
        self.grafo = {}
        self.next_id = 1 
 
    def crear_mundos(self, nombre):
        for mundo in self.grafo.values():
            if mundo['nombre'] == nombre:
                print(f"El mundo '{nombre}' ya existe.")
                return
        mundo_id = self.next_id
        self.grafo[mundo_id] = {'nombre': nombre, 'asociaciones': []}
        self.next_id += 1
        print(f"El mundo '{nombre}' ha sido creado con ID {mundo_id}.")
 
    def asociar_mundos(self, id1, id2):
        if id1 not in self.grafo or id2 not in self.grafo:
            print("Uno o ambos IDs no existen.")
        elif id2 in self.grafo[id1]['asociaciones']:
            print(f"Los mundos con ID {id1} y {id2} ya están asociados.")
        else:
            self.grafo[id1]['asociaciones'].append(id2)
            self.grafo[id2]['asociaciones'].append(id1)
            print(f"Los mundos con ID {id1} y {id2} han sido asociados.")
 
    def eliminar_mundos(self, id):
        if id not in self.grafo:
            print(f"El mundo con ID {id} no existe.")
        else:
            for asociado in self.grafo[id]['asociaciones']:
                self.grafo[asociado]['asociaciones'].remove(id)
            nombre = self.grafo[id]['nombre']
            del self.grafo[id]
            print(f"El mundo '{nombre}' con ID {id} y todas sus asociaciones han sido eliminados.")
 
    def ver_mundos(self):
        print("\nMundos y sus asociaciones:")
        for id, datos in self.grafo.items():
            nombre = datos['nombre']
            asociaciones = [self.grafo[asoc_id]['nombre'] for asoc_id in datos['asociaciones']]
            print(f"ID {id} - {nombre}: {', '.join(asociaciones) if asociaciones else 'Sin asociaciones'}")
 
if __name__ == "__main__":
    grafo = Mundos()
 
    while True:
        print("\n---------------- Kirby the Amazing Mirror ----------------")
        print("1. Crear un mundo")
        print("2. Asociar mundos")
        print("3. Ver mundos y asociaciones")
        print("4. Eliminar un mundo")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del mundo: ")
            grafo.crear_mundos(nombre)
        elif opcion == "2":
            try:
                id1 = int(input("ID del primer mundo: "))
                id2 = int(input("ID del segundo mundo: "))
                grafo.asociar_mundos(id1, id2)
            except ValueError:
                print("Debes ingresar IDs válidos (números enteros).")
        elif opcion == "3":
            grafo.ver_mundos()
        elif opcion == "4":
            try:
                id = int(input("ID del mundo a eliminar: "))
                grafo.eliminar_mundos(id)
            except ValueError:
                print("Debes ingresar un ID válido (número entero).")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")