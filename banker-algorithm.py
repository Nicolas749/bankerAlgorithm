import numpy as np

def banquero(n_procesos, n_recursos, maximo, asignado, disponible):
    # inicialización
    terminado = np.zeros(n_procesos, dtype=bool) #Inicializando en 0 las matrices; False = no finaliza el proceso
    necesidad = maximo - asignado #resta entre las matrices por lo que nos da la matriz de necesidades
    orden = []
    secuencia = []
    
    # ciclo principal
    while len(orden) < n_procesos:
        seguro = False
        
        for i in range(n_procesos):
            if not terminado[i] and np.all(disponible >= necesidad[i]):
                disponible += asignado[i]
                terminado[i] = True
                seguro = True
                orden.append(i)
                secuencia.append('P' + str(i))
        
        if not seguro:
            break
    
    return len(orden) == n_procesos, orden, secuencia

#entradas
n_procesos = 5
n_recursos = 3

# matriz que representa el numero maximo de recursos que cada proceso puede solicitar
# maximo = np.array([[9, 2, 1], [3, 5, 2], [4, 0, 2], [2, 2, 2], [4, 3, 3]]) <-- No es seguro
# maximo = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]) <-- Es seguro
maximo = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])
# matriz que representa la cantidad de recursos que actualmente se le han asignado a cada proceso
asignado = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])

# vector que indica la cantidad de recursos disponibles en el sistema
disponible = np.array([3, 3, 2])

# ejecución del algoritmo del banquero
seguro, orden, secuencia = banquero(n_procesos, n_recursos, maximo, asignado, disponible)

if seguro:
    print("Es seguro asignar los recursos.")
    print("Orden de ejecución de los procesos:", orden)
    print("Secuencia de ejecución de los procesos:", " -> ".join(secuencia))
else:
    print("No es seguro asignar los recursos.")
