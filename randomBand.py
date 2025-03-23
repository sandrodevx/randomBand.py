import random

# Listas de adjetivos y sustantivos
adjetivos = ["Eterno", "Cósmico", "Veloz", "Invisible", "Gigante", "Místico", "Luminoso", "Caótico", "Silencioso", "Infernal"]
sustantivos = ["Dragón", "Espejo", "Laberinto", "Fénix", "Tormenta", "Abismo", "Océano", "Galaxia", "Sombras", "Volcán"]

def generar_nombre_banda():
    # Seleccionar un adjetivo y un sustantivo al azar
    adjetivo = random.choice(adjetivos)
    sustantivo = random.choice(sustantivos)
    
    # Combinar las palabras para formar el nombre de la banda
    nombre_banda = f"{adjetivo} {sustantivo}"
    return nombre_banda

def main():
    print("¡Bienvenido al Generador de Nombres de Bandas Aleatorias!")
    
    while True:
        # Generar y mostrar el nombre de la banda
        nombre = generar_nombre_banda()
        print(f"\nTu nombre de banda es: {nombre}")
        
        # Preguntar al usuario si quiere generar otro nombre
        respuesta = input("\n¿Quieres generar otro nombre? (s/n): ").strip().lower()
        if respuesta != 's':
            print("\n¡Gracias por usar el Generador de Nombres de Bandas! ¡Hasta luego!")
            break

# Ejecutar el programa
if __name__ == "__main__":
    main()