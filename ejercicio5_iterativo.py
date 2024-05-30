def get_int_iterativo():
    """
    Solicita un valor entero al usuario de manera iterativa y lo devuelve.
    
    Retorna:
    int: El valor entero ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input("Ingrese un número entero: "))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def main():
    numero = get_int_iterativo()
    print(f"El número ingresado es: {numero}")

if __name__ == '__main__':
    main()
