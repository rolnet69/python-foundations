import random
import os
import time

# Variables global del tablero
tablero = []
tablero_minas = []
tablero_visible = []
filas = 0
columnas = 0
num_minas = 0
casillas_reveladas = 0
casillas_seguras = 0
primer_jugada = True
juego_activo = True
modo_actual = ""


def generar_minas(filas_cols, num_minas_param):
    """
    Función para generar el tablero con las minas
    """
    global tablero_minas, num_minas
    num_minas = num_minas_param
    minas = [True] * num_minas + [False] * (filas_cols ** 2 - num_minas)
    random.shuffle(minas)
    tablero_minas = [minas[i:i+filas_cols] for i in range(0, len(minas), filas_cols)]
    return tablero_minas


def imprimir_tablero(mostrar_minas_completo=False):
    """
    Imprime el tablero, 
    lo convierte de matriz a algo entendible para el usuario
    """
    # Limpiar pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{'=' * 40}")
    print(f"      BUSCAMINAS - MODO {modo_actual.upper()}")
    print(f"{'=' * 40}")
    
    # Imprimir números de columnas
    print("  ", end="")
    for col in range(1, columnas + 1):
        print(f" {col:2}", end="")
    print()
    print("   " + "-" * (columnas * 3 + 1))
    
    # Imprimir filas con letras
    for fila in range(filas):
        letra_fila = chr(ord('A') + fila)
        print(f"{letra_fila} |", end="")
        
        for col in range(columnas):
            celda = tablero_visible[fila][col]
            
            # Si estamos mostrando todas las minas (al perder)
            if mostrar_minas_completo and tablero_minas[fila][col]:
                print(" * ", end="")
            else:
                if celda == ' ' or celda == '0':
                    print("   ", end="")
                else:
                    print(f" {celda} ", end="")
        print("|")
    
    print("   " + "-" * (columnas * 3 + 1))
    print(f"Minas: {num_minas}")
    print(f"{'=' * 40}")


def generar_tablero():
    """
    Crea el tablero con las filas y columnas numeradas
    inicialmente pone todas las casillas con un punto
    """
    global tablero_visible
    
    tablero_visible = []
    for _ in range(filas):
        fila_tablero = ['.'] * columnas
        tablero_visible.append(fila_tablero)


def iniciar_partida():
    """
    Ajustamos todo para reiniciar una partida,
    en caso que haya terminado recien una
    """
    global tablero_minas, tablero_visible, casillas_reveladas, casillas_seguras, primer_jugada, juego_activo
    
    # Generar minas
    tablero_minas = generar_minas(filas, num_minas)
    
    # Generar tablero visible
    generar_tablero()
    
    # Reiniciar variables de control
    casillas_seguras = filas * columnas - num_minas
    casillas_reveladas = 0
    primer_jugada = True
    juego_activo = True


def buscar_coordenada(coordenada_str):
    """
    Valida que la coordenada exista
    """
    coordenada_str = coordenada_str.strip().upper()
    
    # Validación de formato
    if len(coordenada_str) < 2 or not coordenada_str[0].isalpha() or not coordenada_str[1:].isdigit():
        print("Error: Formato inválido. Use: letra + número (ej. A1)")
        return None, None
    
    letra = coordenada_str[0]
    numero = int(coordenada_str[1:])
    fila_idx = ord(letra) - ord('A')
    
    # Validación de existencia
    if fila_idx < 0 or fila_idx >= filas:
        max_letra = chr(ord('A') + filas - 1)
        print(f"Error: Fila '{letra}' no existe. Rango: A-{max_letra}")
        return None, None
    
    if numero < 1 or numero > columnas:
        print(f"Error: Columna {numero} no existe. Rango: 1-{columnas}")
        return None, None
    
    return fila_idx, numero - 1


def esta_revelada(fila, col):
    """
    Verifica si la coordenada ya ha sido revelada
    """
    return tablero_visible[fila][col] != '.'


def es_mina(fila, col):
    """
    Verifica si una coordenada corresponde a una mina
    """
    return tablero_minas[fila][col]


def vecinos(fila, col):
    """
    Recopila todos los vecinos de una casilla,
    verificando que no invente vecinos,
    osea que no vaya a crear casillas fuera del tablero
    (si la casilla esta en la orilla por ejemplo)
    """
    
    vecinos_lista = []
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            
            nueva_fila = fila + i
            nueva_col = col + j
            
            if 0 <= nueva_fila < filas and 0 <= nueva_col < columnas:
                vecinos_lista.append((nueva_fila, nueva_col))

    # DEBUG: Para ver resultados, descomentar:
    #print(f"[DEBUG] {chr(ord('A')+fila)}{col+1} → {len(vecinos_lista)} vecinos")
    #time.sleep(2) # COMENTAR

    return vecinos_lista


def contar_minas(fila, col):
    """
    Cuenta el numero de minas alrededor de una casilla
    """
    contador = 0
    for vecino_fila, vecino_col in vecinos(fila, col):
        if tablero_minas[vecino_fila][vecino_col]:
            contador += 1
    return contador


def desplazar_mina(fila, col):
    """
    Si es el primer movimiento
    mueve la mina a otra casilla
    """
    global tablero_minas
    
    # Buscar una casilla vacía para desplazas la mina
    for i in range(filas):
        for j in range(columnas):
            if not tablero_minas[i][j] and (i != fila or j != col):
                # Desplazar la mina
                tablero_minas[fila][col] = False
                tablero_minas[i][j] = True
                return True
    
    return False


def mostrar_contenido(fila, col):
    """
    Muestra el contenido de la casilla,
    si tiene minas cercanas solo el valor de cuantas minas hay,
    sino crea una reaccion en cadena.

    (Para el segundo caso)
    Podemos simular una pila para esta reaccion en cadena
    e ir añadiendo los vecinos hasta que no hayan más
    valores libres en el perímetro
    """
    global casillas_reveladas
    
    # Usar una pila para la reacción en cadena
    pila = [(fila, col)]
    
    while pila:
        f_actual, c_actual = pila.pop()
        
        # Si ya está revelado, continuar
        if tablero_visible[f_actual][c_actual] != '.':
            continue
        
        # Contar minas alrededor
        minas_cercanas = contar_minas(f_actual, c_actual)
        
        if minas_cercanas > 0:
            tablero_visible[f_actual][c_actual] = str(minas_cercanas)
            casillas_reveladas += 1
        else:
            tablero_visible[f_actual][c_actual] = ' '
            casillas_reveladas += 1
            
            # Añadir vecinos a la pila
            for vecino_fila, vecino_col in vecinos(f_actual, c_actual):
                if tablero_visible[vecino_fila][vecino_col] == '.':
                    pila.append((vecino_fila, vecino_col))


def mostrar_minas():
    """
    Muestra todas las minas de un tablero
    en caso de perder o terminar la partida
    """
    imprimir_tablero(mostrar_minas_completo=True)


def revelar_coordenada(coordenada):
    """
    Verifica si es una mina,
    si lo es, muestra todas las minas
    sino muestra el contenido de la coordenada
    """
    global juego_activo, primer_jugada
    
    fila, col = coordenada
    
    # Si es la primera jugada y hay mina, desplazarla
    if primer_jugada and tablero_minas[fila][col]:
        desplazar_mina(fila, col)
    
    # Verificar si es mina (después de posible desplazamiento)
    if tablero_minas[fila][col]:
        tablero_visible[fila][col] = '*'
        juego_activo = False
        return False
    
    # Mostrar contenido
    mostrar_contenido(fila, col)
    
    # Marcar que ya no es la primera jugada
    if primer_jugada:
        primer_jugada = False
    
    return True


def pedir_coordenada():
    """
    Pide una coordenada al usuario
    """
    while True:
        entrada = input(f"\nIngrese coordenada (ej. A1) o ingrese 'S' para salir: ").strip().upper()
        
        if entrada == 'S' or entrada == 'SALIR':
            return None
        
        fila, col = buscar_coordenada(entrada)
        
        if fila is None or col is None:
            print("Coordenada inválida. Use formato letra + número, sin espacios ni guiones (ej. A1, B5)")
            continue
        
        if esta_revelada(fila, col):
            print("Esta coordenada ya ha sido revelada. Ingrese otra coordenada.")
            continue
        
        return (fila, col)


def verificar_victoria():
    """Verifica si se han revelado todas las casillas seguras"""
    return casillas_reveladas == casillas_seguras


def partida():
    """
    Mantiene el juego hasta que pierda o gane
    """
    global juego_activo
    
    iniciar_partida()
    
    while juego_activo:
        imprimir_tablero()
        
        # Pedir coordenada
        coordenada = pedir_coordenada()
        
        if coordenada is None:  # Usuario quiere salir
            return False
        
        # Revelar coordenada
        resultado = revelar_coordenada(coordenada)
        
        # Si pisó una mina
        if not resultado:
            mostrar_minas()
            print("\n¡BOOM! ¡Has pisado una mina!")
            print("=" * 40)
            
            while True:
                respuesta = input("¿Quieres jugar otra vez? (S/N): ").upper()
                if respuesta == 'S':
                    return True
                elif respuesta == 'N':
                    return False
                else:
                    print("Por favor, ingrese S ó N")
        
        # Verificar victoria
        if verificar_victoria():
            mostrar_minas()
            print("\n¡FELICIDADES! ¡Has ganado!")
            print("=" * 40)
            
            while True:
                respuesta = input("¿Quieres jugar otra vez? (S/N): ").upper()
                if respuesta == 'S':
                    return True
                elif respuesta == 'N':
                    return False
                else:
                    print("Por favor, ingrese S ó N")
    
    return False


def menu():
    """
    Opciones de inicio
    """
    global filas, columnas, num_minas, modo_actual
    
    while True:
        # Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 40)
        print(" JUEGO DEL BUSCAMINAS - MENÚ PRINCIPAL")
        print("=" * 40)
        print(" ")
        print("Modos de juego:")
        print("1. Modo Normal")
        print("2. Modo Avanzado")
        print("3. Salir del juego")
        print("=" * 40)
        
        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            filas = 9
            columnas = 9
            num_minas = 10
            modo_actual = "Normal"
            print(f"\nIniciando modo {modo_actual}...")
            time.sleep(1)
            
            # Jugar partidas
            continuar_jugando = True
            while continuar_jugando:
                continuar_jugando = partida()
        
        elif opcion == "2":
            filas = 16
            columnas = 16
            num_minas = 25
            modo_actual = "Avanzado"
            print(f"\nIniciando modo {modo_actual}...")
            time.sleep(1)
            
            # Jugar partidas
            continuar_jugando = True
            while continuar_jugando:
                continuar_jugando = partida()
        
        elif opcion == "3":
            print("\n¡Gracias por jugar! Hasta pronto.")
            time.sleep(2)
            # Limpiar pantalla
            os.system('cls' if os.name == 'nt' else 'clear')        
            os._exit(0)
        
        else:
            print("\nOpción inválida. Por favor, seleccione 1, 2 ó 3.")
            time.sleep(1)   


# Ejecutar el juego
menu()