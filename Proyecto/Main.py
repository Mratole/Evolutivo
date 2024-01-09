import numpy as np
import random
import matplotlib.pyplot as plt

population_test = [
    [4, 6],
    [33, 0],
    [11, 22],
    [10, 4],
    [34, 31],
    [16, 9],
    [5, 22],
    [36, 33],
    [44, 36],
    [14, 47],
    [10, 33],
    [4,21],
    [12, 0],
    [7, 4],
    [22, 17],
    [11, 50],
    [17, 22],
    [11,10],
   [10, 2],
   [4, 21],
    [12, 5],
]
Calle_1 = [50, 20, 30, 40, 50, 36, 30, 25, 28, 45, 55, 21, 42, 26, 48, 33, 52, 20, 45, 60, 22, 30, 56, 40, 27, 35, 52, 29, 44, 31]
Calle_2 = [45, 33, 60, 50, 65, 39, 35, 31, 56, 40, 63, 70, 42, 68, 64, 67, 36, 34, 55, 61, 30, 59, 48, 57, 41, 53, 66, 49, 38, 46, 62, 32, 37, 69, 52, 44, 47, 58, 51, 43]
#Calle_1 = [50, 20, 30, 40, 50,30]
#Calle_2 = [10, 20, 30, 40, 50,60,70,90]
num_generaciones=100
Distancia_Cruce = 7
Tamaño_auto= 4.3
Tamano_torneo=2
Distancia_segura=5
Tiempo_inicial = 0
Penalizacion_por_cruce = 3
mejor_individuo = float('inf')
mejor_generacion = 0
promedios = []
mejores = []
menores = []
humano = []
aptitud_humana = 579.5
num_persons = 20

def funcion_aptitud(individuo): 
  
    tiempo1=Tiempo_total_con_conjuntos_calle1(Calle_1,individuo[1],Calle_2)
    tiempo2=tiempo_total_con_conjuntos_calle2(Calle_2,individuo[0],Calle_1)
    tiempo_t=tiempo1+tiempo2/2

    tiempo4=Tiempo_por_conjunto_calle1(Calle_1,individuo[1],Calle_2)
    tiempo5=Tiempo_por_conjunto_calle2(Calle_2,individuo[0],Calle_1)
    tiempo_c=tiempo4+tiempo5/2

    aptitud = calcular_aptitud(tiempo_t,tiempo_c)

    return aptitud



def calcular_aptitud(tiempo_total, tiempo_conjuntos): 
    Valor_tiempo_total = 1
    Valor_tiempo_conjuntos = 19

    aptitud = (Valor_tiempo_conjuntos*tiempo_conjuntos)+(Valor_tiempo_total*tiempo_total)

    return aptitud


def Tiempo_total_con_conjuntos_calle1(individuo,conjunto,auxiliar):
    tiempo = Tiempo_inicial
    distancia = Distancia_Cruce
    Espacio_total=Distancia_segura+Tamaño_auto
    if len(individuo) < len(auxiliar):
        tiempo+=Penalizacion_por_cruce
    for i in range(len(individuo)):
        distancia += Espacio_total
        metros = individuo[i]*1000
        tiempo += distancia/individuo[i]
        if i != 0:
            if conjunto != 0 and i % conjunto == 0:
                tiempo += Penalizacion_por_cruce
    return tiempo

def tiempo_total_con_conjuntos_calle2(individuo,conjunto,auxiliar):
    tiempo = Tiempo_inicial
    distancia = Distancia_Cruce
    Espacio_total=Distancia_segura+Tamaño_auto
    if len(individuo) < len(auxiliar):
        tiempo+=Penalizacion_por_cruce
    for i in range(len(individuo)):
        distancia += Espacio_total
        metros = individuo[i]*1000
        tiempo += distancia/individuo[i]
        if i < len(auxiliar):
            if i != len(individuo):
                if conjunto != 0 and i % conjunto == 0:
                   
                    tiempo += Penalizacion_por_cruce
    return tiempo

def Tiempo_por_conjunto_calle1(individuo, conjunto, auxiliar):
    tiempo = Tiempo_inicial
    distancia = Distancia_Cruce
    Espacio_total=Distancia_segura+Tamaño_auto
    tiempos=[]
    promedio=0
    minimo=0
    if len(individuo) < len(auxiliar):
        tiempo+=Penalizacion_por_cruce
    for i in range(len(individuo)):
        distancia += Espacio_total
        metros = individuo[i]*1000
        tiempo += distancia/individuo[i]
        if i != 0:
            if conjunto != 0 and i % conjunto == 0:
                tiempo += Penalizacion_por_cruce
                tiempos.append(tiempo)
            else:
                tiempos.append(0)
    tiempos.append(tiempo)
    
    for i in reversed(range(len(tiempos))):
        if tiempos[i]!=0:
            temp = tiempos[i]
           
        if tiempos[i]==0:
            tiempos[i]=temp

    minimo = min(tiempos)

    return minimo

def Tiempo_por_conjunto_calle2(individuo, conjunto, auxiliar):
    tiempo = Tiempo_inicial
    distancia = Distancia_Cruce
    Espacio_total=Distancia_segura+Tamaño_auto
    tiempos=[]
    promedio=0
    minimo=0
    if len(individuo) < len(auxiliar):
        tiempo+=Penalizacion_por_cruce
    for i in range(len(individuo)):
        distancia += Espacio_total
        metros = individuo[i]*1000
        tiempo += distancia/individuo[i]
        if i != 0:
            if conjunto != 0 and i % conjunto == 0:
                tiempo += Penalizacion_por_cruce
                tiempos.append(tiempo)
            else:
                tiempos.append(0)
    tiempos.append(tiempo)
    
    for i in reversed(range(len(tiempos))):
        if tiempos[i]!=0:
            temp = tiempos[i]
           
        if tiempos[i]==0:
            tiempos[i]=temp

    minimo = min(tiempos)

    return minimo

def torneo(poblacion, funcion_aptitud, tam_torneo):
    seleccionados = random.sample(poblacion, tam_torneo)
    aptitudes = [funcion_aptitud(individuo) for individuo in seleccionados]
    indice_ganador = aptitudes.index(min(aptitudes))
    return seleccionados[indice_ganador]

def cruce(padre1, padre2):
    hijo1 = np.zeros_like(padre1)
    hijo2 = np.zeros_like(padre2)

    for i in range(len(padre1)):
        if np.random.rand() < 0.5:
            hijo1[i] = padre1[i]
            hijo2[i] = padre2[i]
        else:
            hijo1[i] = padre2[i]
            hijo2[i] = padre1[i]

    probabilidad = np.random.randint(0, 100)
    if 0 < probabilidad <= 70:
        return hijo1, hijo2
    else:
        return padre1, padre2

def mutacion(individuo):
    for i in range(len(individuo)):
        probabilidad_mutacion = np.random.randint(0, 1000)
        if probabilidad_mutacion <=110:
            individuo[i] = np.random.randint(0, 35)
    return individuo

for generacion in range(num_generaciones):
    print(f'Generación {generacion + 1}')

    aptitudes = [funcion_aptitud(individuo) for individuo in population_test]

    promedio = sum(aptitudes) / len(aptitudes)
    mejor = max(aptitudes)
    menor = min(aptitudes)
    if mejor_individuo > min(aptitudes):
        mejor_individuo = min(aptitudes)
        mejor_generacion = generacion

    promedios.append(promedio)
    mejores.append(mejor)
    menores.append(menor)
    humano.append(aptitud_humana)
    print(f'Promedio de aptitud: {promedio:.2f}')
    print(f'Peor aptitud: {mejor:.2f}')
    print(f'Mejor aptitud: {menor:.2f}')
    print(f'Mejor individuo: {mejor_individuo:.2f}')
    

    nueva_poblacion = []
    for _ in range(num_persons // 2):
        padre1 = torneo(population_test, funcion_aptitud, Tamano_torneo)
        padre2 = torneo(population_test, funcion_aptitud, Tamano_torneo)

        hijo1, hijo2 = cruce(padre1, padre2)

        hijo1 = mutacion(hijo1)
        hijo2 = mutacion(hijo2)

        nueva_poblacion.extend([hijo1, hijo2])
    population_test = nueva_poblacion


plt.plot(promedios, label='Promedio')
plt.plot(menores, label='Mejores')
plt.plot(mejores, label='Peores')
plt.plot(humano, label='Humano')
plt.scatter(mejor_generacion, mejor_individuo, color='red', label=f'Mejor valor: {mejor_individuo:.2f}')
plt.xlabel('Numero de generación')
plt.ylabel('Aptitud')
plt.legend()
plt.show()
