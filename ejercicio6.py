class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def set_nombre(self, nombre):
        while True:
            if isinstance(nombre, str) and nombre.strip() != "":
                if nombre.isalpha():
                    self.nombre = nombre
                    break
                else:
                    print("Error: El nombre solo puede contener letras.")
            else:
                print("Error: El nombre debe ser una cadena de caracteres no vacía.")
            nombre = input("Ingrese el nombre nuevamente: ")
    
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        while True:
            try:
                edad = int(edad)  # Convertir a entero
                if 0 <= edad <= 150:
                    self.edad = edad
                    break
                else:
                    print("Error: La edad debe estar entre 0 y 150 años.")
                    edad = input("Ingrese la edad nuevamente: ")
            except ValueError:
                print("Error: Por favor, ingrese un número entero para la edad.")
                edad = input("Ingrese la edad nuevamente: ")
    
    def get_edad(self):
        return self.edad
    
    def set_dni(self, dni):
        while True:
            if isinstance(dni, str) and len(dni) == 8 and dni.isdigit():
                self.dni = dni
                break
            else:
                print("Error: El DNI debe ser una cadena de 8 dígitos numéricos.")
                dni = input("Ingrese el DNI nuevamente: ")
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

def main():
    # Crear una instancia de Persona
    persona1 = Persona()
    
    # Solicitar y validar el nombre
    persona1.set_nombre(input("Ingrese el nombre: "))
    
    # Solicitar y validar la edad
    persona1.set_edad(input("Ingrese la edad: "))
    
    # Solicitar y validar el DNI
    persona1.set_dni(input("Ingrese el DNI: "))
    
    # Mostrar los datos de la persona
    persona1.mostrar()
    
    # Verificar si es mayor de edad
    if persona1.es_mayor_de_edad():
        print("La persona es mayor de edad.")
    else:
        print("La persona no es mayor de edad.")

if __name__ == "__main__":
    main()
