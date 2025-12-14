def findSmallest(arr):
    smallest = arr[0]       # Almacena el valor más pequeño
    smallest_index = 0      # Almacena el índice del valor más pequeño
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)   # Copia el arrar antes de mutar
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([0, 5, 3, 6, 2, 10]))
