import random
import time

from metodos_ordenamiento import MetodoOrdenanmiento

class Benchmarking:
    def __init__(self):
        print('Bench inicializado')
        self.mOrdenamiento = MetodoOrdenanmiento()
        arreglo = self.build_arreglo(1000)

        tarea = lambda:self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)

        print(f'Tiempo {tiempoMillis}')
        print(f'Tiempo{tiempoNano}')
    
    def build_arreglo(self, tamanio):
        array = []
        for i in range(tamanio):
            numero = random.randint(0, 99999)
            array.append(numero)
        return array
    
    #import time
    #ejecutar  tarea tarea()

    # x = time.time()
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        fin = time.time()
        return fin - inicio
    
    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio)/ 1_000_000_000.0
