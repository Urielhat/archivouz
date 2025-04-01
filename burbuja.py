def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compara los elementos de cada casilla
            if arr[j] > arr[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                arr[j], arr[j+1] = arr[j+1], arr[j]


lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista)
print("Lista ordenada:", lista)