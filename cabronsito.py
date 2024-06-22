
# Definimos el mapeo de coordenadas a letras usando la disposición de la imagen
qwerty_keyboard = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ñ'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '', '', '']
]

# Crear un diccionario inverso para cifrar
char_to_coords = {}
for fila in range(len(qwerty_keyboard)):
    for columna in range(len(qwerty_keyboard[fila])):
        char = qwerty_keyboard[fila][columna]
        if char:  # Evita las celdas vacías
            char_to_coords[char] = f'({fila}{columna})'

def descifrar_qwerty(coordenadas):
    """
    Descifra un texto basado en coordenadas del teclado QWERTY según la imagen proporcionada.
    
    Args:
    coordenadas (str): Coordenadas en formato (XY) separadas por espacios.
    
    Returns:
    str: Texto descifrado
    """
    texto_descifrado = []
    coordenadas = coordenadas.split()  # Divide las coordenadas por espacios
    for coord in coordenadas:
        coord = coord.strip('()')
        fila, columna = int(coord[0]), int(coord[1])
        if 0 <= fila < len(qwerty_keyboard) and 0 <= columna < len(qwerty_keyboard[fila]):
            texto_descifrado.append(qwerty_keyboard[fila][columna])
        else:
            texto_descifrado.append('?')  # Para coordenadas fuera de rango
    return ''.join(texto_descifrado)

def cifrar_qwerty(texto):
    """
    Cifra un texto en coordenadas del teclado QWERTY según la imagen proporcionada.
    
    Args:
    texto (str): Texto a cifrar.
    
    Returns:
    str: Texto cifrado en formato de coordenadas.
    """
    texto_cifrado = []
    for char in texto.upper():
        if char in char_to_coords:
            texto_cifrado.append(char_to_coords[char])
        else:
            texto_cifrado.append('(??)')  # Para caracteres no encontrados en el teclado
    return ' '.join(texto_cifrado)

def main():
    """
    Función principal que permite al usuario elegir entre cifrar y descifrar.
    """
    while True:
        # Solicitar al usuario que elija cifrar o descifrar
        opcion = input("elige una opción cabronsito: (c) Cifrar, (d) Descifrar: ").strip().lower()
        if opcion == 'c':
            # Opción de cifrado
            texto = input("introduce el texto a cifrar cabronsito: ").strip()
            texto_cifrado = cifrar_qwerty(texto)
            print("Texto cifrado:", texto_cifrado)
        elif opcion == 'd':
            # Opción de descifrado
            coordenadas = input("Introduce las coordenadas a descifrar (formato: (XY) separados por espacios): ").strip()
            texto_descifrado = descifrar_qwerty(coordenadas)
            print("Texto descifrado:", texto_descifrado)
        else:
            print("pinche cabronsito no esta bien. Por favor, elige 'c' para cifrar o 'd' para descifrar.")

        # Preguntar si se desea continuar
        continuar = input("¿Quieres realizar otra operación cabronsito? (s/n): ").strip().lower()
        if continuar != 's':
            print("nos vemos cabronsito")
            break

# Ejecutar la función principal
if __name__ == "__main__":
    main()
