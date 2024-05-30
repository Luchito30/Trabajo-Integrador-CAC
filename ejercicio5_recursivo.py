def get_int_recursivo():
    """
    Solicita un valor entero al usuario de manera recursiva y lo devuelve.
    
    Retorna:
    int: El valor entero ingresado por el usuario.
    """
    try:
        valor = int(input("Ingrese un número entero: "))
        return valor
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
        return get_int_recursivo()

def main():
    numero = get_int_recursivo()
    print(f"El número ingresado es: {numero}")

if __name__ == '__main__':
    main()
