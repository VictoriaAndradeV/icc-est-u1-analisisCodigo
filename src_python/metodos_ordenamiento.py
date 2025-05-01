class MetodoOrdenanmiento:

    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[i], arreglo[i]
                    #temp = arreglo[i]
                    #arreglo[i] = arreglo[j]
                    #arreglo[j] = temp
        return arreglo
    
    def selecctionSort(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            indiceMin = i 
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[indiceMin]:
                    indiceMin = j 

            if indiceMin != i:
                aux = arreglo[i]
                arreglo[i] = arreglo[indiceMin]
                arreglo[indiceMin] = aux

        return arreglo 

            


