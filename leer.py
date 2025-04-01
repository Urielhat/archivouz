def analizar_y_encontrar(Nombrepruebaarcvito, Palabra_encontrar, palabra_averiguar, nuevo_archivito=None):
    
    try:
        with open(Nombrepruebaarcvito, 'r', encoding='utf-8') as archivito:
            contenido = archivito.read()
        
        contenido_modificado = contenido.replace(Palabra_encontrar, palabra_averiguar)
        
        arcvito_salida = nuevo_archivito if nuevo_archivito else Nombrepruebaarcvito
        
        with open(arcvito_salida, 'w', encoding='utf-8') as archivito:
            archivito.write(contenido_modificado)
            
        print(f" **Se reemplazó** '{Palabra_encontrar}' por '{palabra_averiguar}' en '{arcvito_salida}'.")
    except FileNotFoundError:
        print(f" Error: El archivito '{Nombrepruebaarcvito}' no existe.")
    except Exception as e:
        print(f" Ocurrió un error: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    print("////buscar y encontrar archivito TXT////// ")
    archivito = input("Ingresa la ruta donde tengas el archivito seguido por \su nombre.txt(ej: 'datos.txt'): ")
    buscar = input("Palabra a buscar: ")
    reemplazar = input("Palabra de cambio: ")
    opcion = input("¿Guardar en nuevo archivito? (s/n): ").strip().lower()
    
    nuevo_archivito = None
    if opcion == 's':
        nuevo_archivito = input("ingresa la ruta donde quieres que se guarde el archivito seguido por \su nuevo nombre.txt (ej: 'modificado.txt'): ")
    
    analizar_y_encontrar(archivito, buscar, reemplazar, nuevo_archivito)