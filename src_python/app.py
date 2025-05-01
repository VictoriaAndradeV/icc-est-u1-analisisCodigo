#import benchmarcking as Ben
from benchmarcking import Benchmarking
from metodos_ordenamiento import MetodoOrdenanmiento

if __name__=="__main__":
    print("funciona")

    #Instancias
    metodoO = MetodoOrdenanmiento()
    benchmark = Benchmarking()

    tama = 10000
    arreglo_base = benchmark.build_arreglo(tama)

    #diccionario con dos elementos, clave y metodo de ordenamiento
    #si pongo parentesis luego de la funcion se ejecuta

    metodos = {
        "Burbuja": MetodoOrdenanmiento.sortByBubble,
        "Seleccion": MetodoOrdenanmiento.selectionSort
    }


    #.items me da una tupla
    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = benchmark.medir_tiempo(metodo, arreglo_base)
        tuplaResultado = (tama, nombre, tiempo) #datos que no quiero que se dañen 
        resultados.append(tuplaResultado)

    for resultado in resultados:
        tama, nombre, tiempo = resultado #variables de tupla en variables diferentes
        print(f"Tamanio: {tama}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")