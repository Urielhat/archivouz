def ordenamiento_insercion(arr):
    for i in range(1, len(arr)):
        valor_actual = arr[i]
        j = i - 1
        while j >= 0 and valor_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = valor_actual
    return arr

def main():
    datos = input("Ingresa una lista de números separados por espacios: ")
    lista = list(map(int, datos.split()))
    lista_ordenada = ordenamiento_insercion(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
