""" función que calcule el mínimo común múltiplo entre dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """


def mcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n


def mcm(a,b):
    return a * b // mcd(a, b)


def main():

    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    print("El valor es: ", mcm(a, b))
    return None

if __name__ == '__main__':
    main()