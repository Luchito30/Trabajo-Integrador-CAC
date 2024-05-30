"""
    Recibe una cadena de caracteres y devuelve un diccionario con cada palabra y su frecuencia.
    
    Parámetros:
    cadena (str): La cadena de caracteres.
    
    Retorna:
    dict: Un diccionario donde las claves son las palabras y los valores son las frecuencias.
    """

import string

def contar_palabras(cadena):
    
    # Convertir la cadena a minúsculas
    cadena = cadena.lower()
    
    # Eliminar signos de puntuación, incluyendo '¿' y '¡'
    for char in '¿¡' + string.punctuation:
        cadena = cadena.replace(char, "")
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

def main():
    cadena = input("Ingrese la cadena: ")
    resultado = contar_palabras(cadena)
    print(resultado)

if __name__ == '__main__':
    main()
