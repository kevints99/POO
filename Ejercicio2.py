class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificacion: {self.calificacion}")
    
    def verificar_aprobacion(self):
        if self.calificacion >= 3.5:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha reprobado.")

# Ejemplo de uso
estudiante1 = Estudiante("Kevin Tapia", 20, 4.2)
estudiante1.mostrar_informacion()
estudiante1.verificar_aprobacion()

estudiante2 = Estudiante("Luzdey Carbal", 19, 2.8)
estudiante2.mostrar_informacion()
estudiante2.verificar_aprobacion()
