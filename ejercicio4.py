import string

def contar_palabras(cadena):
    """
    Recibe una cadena de caracteres y devuelve un diccionario con cada palabra y su frecuencia.
    
    Parámetros:
    cadena (str): La cadena de caracteres.
    
    Retorna:
    dict: Un diccionario donde las claves son las palabras y los valores son las frecuencias.
    """
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

def palabra_mas_repetida(diccionario):
    """
    Recibe un diccionario con palabras y sus frecuencias y devuelve una tupla con la palabra más repetida y su frecuencia.
    
    Parámetros:
    diccionario (dict): Un diccionario donde las claves son las palabras y los valores son las frecuencias.
    
    Retorna:
    tuple: Una tupla con la palabra más repetida y su frecuencia.
    """
    # Encontrar la palabra más repetida
    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    frecuencia = diccionario[palabra_mas_repetida]
    
    return (palabra_mas_repetida, frecuencia)

def main():
    cadena = input("Ingrese la cadena: ")
    diccionario_frecuencia = contar_palabras(cadena)
    print("Diccionario de frecuencias:", diccionario_frecuencia)
    palabra, frecuencia = palabra_mas_repetida(diccionario_frecuencia)
    print(f"La palabra más repetida es '{palabra}' con una frecuencia de {frecuencia}.")

if __name__ == '__main__':
    main()
