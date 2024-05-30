import json
from ejercicio7 import *

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def es_titular_valido(self, edad):
        return 18 <= edad < 25
    
    def mostrar(self):
        super().mostrar()  # Llama al método mostrar() de la clase padre
        print(f"Cuenta Joven\nBonificación: {self.bonificacion}%")

def cargar_beneficios():
    try:
        with open("beneficios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def asignar_beneficios(cuentas, beneficios):
    for id_cuenta, cuenta in cuentas.items():
        if id_cuenta in beneficios:
            cuenta["bonificacion"] = beneficios[id_cuenta]["bonificacion"]

def guardar_beneficios(beneficios):
    with open("beneficios.json", "w") as file:
        json.dump(beneficios, file, indent=4)
        
def solicitar_bonificacion():
    while True:
        try:
            bonificacion = float(input("Ingrese la bonificación (%): "))
            if 0 <= bonificacion <= 100:
                return bonificacion
            else:
                print("Error: La bonificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la bonificación.")
            
def solicitar_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad del titular: "))
            if edad >= 0:
                return edad
            else:
                print("Error: La edad debe ser un número positivo.")
        except ValueError:
            print("Error: Por favor, ingrese una edad válida.")

def mostrar_opciones():
    print("Seleccione una opción:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Cambiar/Crear un nuevo titular")
    print("4. Modificar titular existente")
    print("5. Modificar bonificación")
    print("6. Eliminar titular")
    print("7. Finalizar")
        
def main():
    cuentas = cargar_cuentas()
    beneficios = cargar_beneficios()
    asignar_beneficios(cuentas, beneficios)

    while True:
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        while not titular.isalpha():
            print("Error: El titular debe contener solo letras.")
            titular = input("Ingrese el nombre del titular de la cuenta nuevamente: ")

        cuenta_existente = None
        for id_cuenta, cuenta in cuentas.items():
            if cuenta["titular"] == titular:
                cuenta_existente = cuenta
                break

        if cuenta_existente:
            id_cuenta = id_cuenta
            cuenta_joven = CuentaJoven(titular, cuenta_existente["cantidad"], cuenta_existente["bonificacion"])
            cuenta_joven.mostrar()
        else:
            bonificacion = solicitar_bonificacion()
            if bonificacion is None:
                print("La bonificación debe ser un número entre 0 y 100.")
                continue
            edad = solicitar_edad()
            nuevo_titular = CuentaJoven(titular)
            if nuevo_titular.es_titular_valido(edad):
                cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la cuenta: ")
                id_cuenta = obtener_id_disponible(cuentas)
                cuentas[id_cuenta] = {"titular": titular, "cantidad": cantidad_inicial, "bonificacion": bonificacion}
                print("Cuenta creada correctamente.")
                cuenta_joven = CuentaJoven(titular, cantidad_inicial, bonificacion)
                cuenta_joven.mostrar()
                guardar_cuentas(cuentas)
            else:
                print("El titular no cumple con la edad para crear una cuenta joven.")
                # Volver al menú principal manteniendo los datos del titular anterior
                continue

        while True:
            mostrar_opciones()
            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                cantidad = solicitar_cantidad("Ingrese la cantidad a ingresar en la cuenta: ")
                cuentas[id_cuenta]["cantidad"] += cantidad
                print("Cantidad Ingresada correctamente.")
                print(f"Titular: {cuentas[id_cuenta]['titular']}")
                print(f"Cantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
                print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
                guardar_cuentas(cuentas)
            elif opcion == "2":
                cantidad = solicitar_cantidad("Ingrese la cantidad a retirar de la cuenta: ")
                cuentas[id_cuenta]["cantidad"] -= cantidad
                print("Cantidad retirada correctamente.")
                titular_actual = cuentas[id_cuenta]["titular"]
                print(f"Titular: {titular_actual}\nCantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
                print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
                guardar_cuentas(cuentas)
            elif opcion == "3":
                nuevo_titular = input("Ingrese el nombre del titular de la cuenta: ")
                while not nuevo_titular.isalpha():
                    print("Error: El titular debe contener solo letras.")
                    nuevo_titular = input("Ingrese el nombre del titular de la cuenta nuevamente: ")
                
                cuenta_existente = None
                for id_cuenta, cuenta in cuentas.items():
                    if cuenta["titular"] == nuevo_titular:
                        cuenta_existente = cuenta
                        break
                
                if cuenta_existente:
                    cuenta_joven = CuentaJoven(nuevo_titular, cuenta_existente["cantidad"], cuenta_existente["bonificacion"])
                    cuenta_joven.mostrar()
                else:
                    print("No se encontró el titular. Se creará una nueva cuenta.")
                    bonificacion = solicitar_bonificacion()
                    if bonificacion is None:
                        print("La bonificación debe ser un número entre 0 y 100.")
                        continue
                    edad = solicitar_edad()
                    nuevo_titular = CuentaJoven(titular)
                    if nuevo_titular.es_titular_valido(edad):
                        cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la cuenta: ")
                        id_cuenta = obtener_id_disponible(cuentas)
                        cuentas[id_cuenta] = {"titular": titular, "cantidad": cantidad_inicial, "bonificacion": bonificacion}
                        print("Cuenta creada correctamente.")
                        cuenta_joven = CuentaJoven(titular, cantidad_inicial, bonificacion)
                        cuenta_joven.mostrar()
                        guardar_cuentas(cuentas)
                    else:
                        print("El titular no cumple con la edad para crear una cuenta joven.")
                        # Volver al menú principal manteniendo los datos del titular anterior
                        print(f"Esta en Ultimo Titular: {cuentas[id_cuenta]['titular']}")
                        print(f"Cantidad: {cuentas[id_cuenta]['cantidad']}")
                        print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
            elif opcion == "4":
                while True:
                    nombre_titular = input("Ingrese el nombre del titular de la cuenta: ")
                    while not nombre_titular.isalpha():
                        print("Error: El titular debe contener solo letras.")
                        nombre_titular = input("Ingrese el nombre del titular de la cuenta nuevamente: ")

                    cuenta_existente = None
                    for id_cuenta, cuenta in cuentas.items():
                        if cuenta["titular"] == nombre_titular:
                            cuenta_existente = cuenta
                            break

                    if cuenta_existente:
                        nuevo_nombre = input("Ingrese el nuevo nombre del titular: ")
                        while not nuevo_nombre.isalpha():
                            print("Error: El titular debe contener solo letras.")
                            nuevo_nombre = input("Ingrese el nuevo nombre del titular nuevamente: ")
                        print(f"Titular actual: {cuenta_existente['titular']}")
                        cuentas[id_cuenta]['titular'] = nuevo_nombre
                        guardar_cuentas(cuentas)
                        print(f"El titular anterior '{nombre_titular}' ha sido cambiado a '{nuevo_nombre}'.")
                        print(f"Esta operando con el Titular: {cuentas[id_cuenta]['titular']}")
                        
                        while True:
                            mostrar_submenu_modificar_titular()
                            sub_opcion = input("Ingrese su opción: ")

                            if sub_opcion == "1":
                                break  # Volver a ingresar el titular
                            elif sub_opcion == "2":
                                print(f"Operando con el titular: {cuentas[id_cuenta]['titular']}\nCantidad: {cuentas[id_cuenta]['cantidad']}")
                                print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
                                break  # Volver al menú principal
                            elif sub_opcion == "3":
                                print("Programa finalizado.")
                                return
                            else:
                                print("Error: Opción inválida. Por favor, seleccione una opción válida.")
                        if sub_opcion == "1":
                            continue
                        break
                    else:
                        print("No se encontró el titular en el sistema.")
                        crear_nuevo = input("¿Desea crear una nueva cuenta para este titular? (s/n): ").lower()
                        while crear_nuevo not in ["s", "n"]:
                            print("Error: Por favor, ingrese 's' para sí o 'n' para no.")
                            crear_nuevo = input("¿Desea crear una nueva cuenta para este titular? (s/n): ").lower()

                        if crear_nuevo == "s":
                            cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la nueva cuenta: ")
                            # Generar nuevo id
                            id_cuenta = obtener_id_disponible(cuentas)
                            cuentas[id_cuenta] = {"titular": nombre_titular, "cantidad": cantidad_inicial}
                            print("Cuenta creada correctamente.")
                            print(f"Titular: {nombre_titular}\nCantidad: {cantidad_inicial}")
                            print(f"Bonificación: {cuentas[id_cuenta]['bonificacion']}")
                            guardar_cuentas(cuentas)
                            break  # Volver al menú principal
                        else:
                            continue  # Volver a ingresar el titular
                pass
            elif opcion == "5":
                bonificacion = solicitar_bonificacion()
                if bonificacion is None:
                    print("La bonificación debe ser un número entre 0 y 100.")
                    continue
                cuentas[id_cuenta]["bonificacion"] = bonificacion
                print(f"Bonificación modificada correctamente: {cuentas[id_cuenta]['bonificacion']}%")
                print(f"Titular: {cuentas[id_cuenta]['titular']}")
                print(f"Cantidad: {cuentas[id_cuenta]['cantidad']}")
                print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
                guardar_cuentas(cuentas)
            elif opcion == "6":
                while True:
                    nombre_titular = input("Ingrese el nombre del titular que desea eliminar: ")
                    while not nombre_titular.isalpha():
                        print("Error: El titular debe contener solo letras.")
                        nombre_titular = input("Ingrese el nombre del titular nuevamente: ")

                    cuenta_existente = None
                    for id_cuenta, cuenta in cuentas.items():
                        if cuenta["titular"] == nombre_titular:
                            cuenta_existente = cuenta
                            break

                    if cuenta_existente:
                        del cuentas[id_cuenta]
                        guardar_cuentas(cuentas)
                        print(f"La cuenta del titular '{nombre_titular}' ha sido eliminada.")
                        
                        while True:
                            # Reiniciar el ciclo principal para ingresar/crear nuevo titular
                            titular = input("Ingrese el nombre del titular de la cuenta a buscar o crear: ")
                            while not titular.isalpha():
                                print("Error: El titular debe contener solo letras.")
                                titular = input("Ingrese el nombre del titular de la cuenta nuevamente: ")

                            cuenta_existente = None
                            for id_cuenta, cuenta in cuentas.items():
                                if cuenta["titular"] == titular:
                                    cuenta_existente = cuenta
                            break

                        if cuenta_existente:
                            id_cuenta = id_cuenta
                            cuenta_joven = CuentaJoven(titular, cuenta_existente["cantidad"], cuenta_existente["bonificacion"])
                            cuenta_joven.mostrar()
                        else:
                            bonificacion = solicitar_bonificacion()
                            if bonificacion is None:
                                print("La bonificación debe ser un número entre 0 y 100.")
                                continue
                            edad = solicitar_edad()
                            nuevo_titular = CuentaJoven(titular)
                            if nuevo_titular.es_titular_valido(edad):
                                cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la cuenta: ")
                                id_cuenta = obtener_id_disponible(cuentas)
                                cuentas[id_cuenta] = {"titular": titular, "cantidad": cantidad_inicial, "bonificacion": bonificacion}
                                print("Cuenta creada correctamente.")
                                cuenta_joven = CuentaJoven(titular, cantidad_inicial, bonificacion)
                                cuenta_joven.mostrar()
                                guardar_cuentas(cuentas)
                            else:
                                print("El titular no cumple con la edad para crear una cuenta joven.")
                                # Volver al menú principal manteniendo los datos del titular anterior
                                print(f"Esta en Ultimo Titular: {cuentas[id_cuenta]['titular']}")
                                print(f"Cantidad: {cuentas[id_cuenta]['cantidad']}")
                                print(f"Cuenta Joven\nBonificación: {cuentas[id_cuenta]['bonificacion']}%")
                            break
                        break
                    else:
                        while True:
                            print("No se encontró el titular.")
                            mostrar_submenu_eliminar_titular()
                            sub_opcion = input("Ingrese su opción: ")
                            
                            if sub_opcion == "1":
                                break  # Intentar eliminar de nuevo
                            elif sub_opcion == "2":
                                print("Programa finalizado.")
                                return
                            else:
                                print("Error: Opción inválida. Por favor, seleccione una opción válida.")
                        if sub_opcion == "1":
                            continue
                            break
                        elif opcion == "7":
                            print("Programa finalizado.")
                            return
                        else:
                            print("Error: Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

