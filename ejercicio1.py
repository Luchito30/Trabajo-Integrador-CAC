"""Función que calcule el máximo común divisor entre dos números.
    Parámetros:
        - num1: Es un número entero.
        - num2: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """

import math


def divisorComunMayor(num1, num2):
    
    mcd = math.gcd(num1, num2)
    print("El MCD de", num1, "y", num2, "es:", mcd)
    return None


def main():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el primer numero: "))
    divisorComunMayor(num1 , num2)
    return None


if __name__ == '__main__':
    main()