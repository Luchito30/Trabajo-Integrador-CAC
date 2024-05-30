import json

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad  # Atributo privado
    
    def set_titular(self, titular):
        while True:
            if isinstance(titular, str) and titular.strip() != "" and titular.isalpha():
                self.titular = titular
                break
            else:
                print("Error: El titular debe ser una cadena de caracteres no vacía y solo letras.")
                titular = input("Ingrese el nombre del titular de la cuenta nuevamente: ")
    
    def get_titular(self):
        return self.titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        while True:
            try:
                cantidad = float(cantidad)
                if cantidad > 0:
                    self.__cantidad += cantidad
                    break
                else:
                    print("Error: La cantidad ingresada debe ser un número positivo.")
                    cantidad = input("Ingrese la cantidad a ingresar en la cuenta nuevamente: ")
            except ValueError:
                print("Error: Por favor, ingrese un número para la cantidad.")
                cantidad = input("Ingrese la cantidad a ingresar en la cuenta nuevamente: ")
    
    def retirar(self, cantidad):
        while True:
            try:
                cantidad = float(cantidad)
                if cantidad > 0 and cantidad <= self.__cantidad:
                    self.__cantidad -= cantidad
                    break
                elif cantidad <= 0:
                    print("Error: La cantidad ingresada debe ser un número positivo.")
                    cantidad = input("Ingrese la cantidad a retirar de la cuenta nuevamente: ")
                else:
                    print("Error: La cantidad ingresada excede el saldo disponible en la cuenta.")
                    cantidad = input("Ingrese una cantidad menor o igual al saldo disponible: ")
            except ValueError:
                print("Error: Por favor, ingrese un número para la cantidad.")
                cantidad = input("Ingrese la cantidad a retirar de la cuenta nuevamente: ")

class Persona:
    def __init__(self, nombre=""):
        self.nombre = nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

def cargar_cuentas():
    try:
        with open("cuentas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_cuentas(cuentas):
    for cuenta in cuentas.values():
        if "bonificacion" not in cuenta:
            cuenta["bonificacion"] = None
            
    with open("cuentas.json", "w") as file:
        json.dump(cuentas, file, indent=4)

def obtener_id_disponible(cuentas):
    return f"id{len(cuentas) + 1}"

def mostrar_opciones():
    print("Seleccione una opción:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Cambiar/Crear un nuevo titular")
    print("4. Modificar titular existente")
    print("5. Eliminar titular")
    print("6. Finalizar")

def solicitar_cantidad(mensaje):
    while True:
        try:
            cantidad = float(input(mensaje))
            return cantidad
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la cantidad.")

def mostrar_submenu_modificar_titular():
    print("\nSubmenú - Modificar titular existente:")
    print("1. Modificar otro titular")
    print("2. Volver al menú principal")
    print("3. Finalizar")

def mostrar_submenu_eliminar_titular():
    print("\nSubmenú - Eliminar titular:")
    print("1. Intentar eliminar titular")
    print("2. Finalizar")

def main():
    # Cargar cuentas existentes
    cuentas = cargar_cuentas()
    
    while True:
        # Solicitar titular de la cuenta
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
            id_cuenta = id_cuenta  # Establecer id_cuenta si el titular ya existe
            print(f"Titular: {cuenta_existente['titular']}\nCantidad: {cuenta_existente['cantidad']}")
        else:
            cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la cuenta: ")
            # Generar nuevo id
            id_cuenta = obtener_id_disponible(cuentas)
            cuentas[id_cuenta] = {"titular": titular, "cantidad": cantidad_inicial}
            print("Cuenta creada correctamente.")
            print(f"Titular: {cuentas[id_cuenta]['titular']}")
            print(f"Cantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
            guardar_cuentas(cuentas)

        while True:
            # Mostrar opciones disponibles
            mostrar_opciones()

            opcion = input("Ingrese su opción: ")
            
            if opcion == "1":
                cantidad = solicitar_cantidad("Ingrese la cantidad a ingresar en la cuenta: ")
                cuentas[id_cuenta]["cantidad"] += cantidad
                print(f"Titular: {cuentas[id_cuenta]['titular']}")
                print(f"Cantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
                guardar_cuentas(cuentas)
            elif opcion == "2":
                cantidad = solicitar_cantidad("Ingrese la cantidad a retirar de la cuenta: ")
                cuentas[id_cuenta]["cantidad"] -= cantidad
                print("Cantidad retirada correctamente.")
                guardar_cuentas(cuentas)
                titular_actual = cuentas[id_cuenta]["titular"]
                print(f"Titular: {titular_actual}\nCantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
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
                    print(f"Titular: {cuenta_existente['titular']}\nCantidad: {cuenta_existente['cantidad']}")
                else:
                    print("No se encontró el titular. Se creará una nueva cuenta.")
                    cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la nueva cuenta: ")
                    # Generar nuevo id
                    id_cuenta = obtener_id_disponible(cuentas)
                    cuentas[id_cuenta] = {"titular": nuevo_titular, "cantidad": cantidad_inicial}
                    print("Cuenta creada correctamente.")
                    print(f"Titular: {nuevo_titular}\nCantidad: {cantidad_inicial}")
                
                guardar_cuentas(cuentas)
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
                            guardar_cuentas(cuentas)
                            break  # Volver al menú principal
                        else:
                            continue  # Volver a ingresar el titular
            elif opcion == "5":
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
                                id_cuenta = id_cuenta  # Establecer id_cuenta si el titular ya existe
                                print(f"Titular: {cuenta_existente['titular']}\nCantidad: {cuenta_existente['cantidad']}")
                            else:
                                cantidad_inicial = solicitar_cantidad("Ingrese la cantidad inicial para la cuenta: ")
                                # Generar nuevo id
                                id_cuenta = obtener_id_disponible(cuentas)
                                cuentas[id_cuenta] = {"titular": titular, "cantidad": cantidad_inicial}
                                print("Cuenta creada correctamente.")
                                print(f"Titular: {cuentas[id_cuenta]['titular']}")
                                print(f"Cantidad actualizada: {cuentas[id_cuenta]['cantidad']}")
                                guardar_cuentas(cuentas)
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
            elif opcion == "6":
                print("Programa finalizado.")
                return
            else:
                print("Error: Opción inválida. Por favor, seleccione una opción válida.")
                continue

if __name__ == "__main__":
    main()
