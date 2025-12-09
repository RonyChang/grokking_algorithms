# Quiero usar una lista ordenada y encontrar el número deseado
# en el menor número de iteraciones posibles.

def obtener_numero_deseado(lista, numero):      # Binary_search
    low = 0                     # Posición del primer número
    high = len(lista) - 1       # Posición del último número
    while low <= high:
        mid = (low + high) // 2 # Posición del número del medio
        guess = lista[mid]      # Numero del medio.
        if guess == numero:
            return mid
        elif guess < numero:
            low = mid + 1
        else:
            high = mid - 1
    return None

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(obtener_numero_deseado(lista, 13)) # Me da la posición 12

print(obtener_numero_deseado(lista, -5))