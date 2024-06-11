import random
import math


def poisson(p, corridas):
    resultados = []
    for _ in range(corridas):
        x = 0
        b = math.exp(-p)
        tr = 1.0
        while True:
            r = random.random()
            tr *= r
            if tr < b:
                break
            x += 1
        resultados.append(x)
    return resultados

def uniform(a, b):
    r = random.random()
    x = a + (b - a) * r
    x_rounded = round(x, 10)
    return x_rounded

#NORMAL
def normal(ex, stdx, corridas):
    resultados = []
    for _ in range(corridas):
        suma = 0.0
        for i in range(12):
            r = random.random()
            suma += r
        x = stdx * (suma - 6.0) + ex
        resultados.append(x)
    return resultados



def binomial_distribution(n, p, size):
    result = []
    for _ in range(size):
        # Generar n variables uniformes y transformarlas a variables de Bernoulli
        successes = sum(random.random() < p for _ in range(n))
        result.append(successes)
    return result



def expent(ex, corridas):
    resultados = []
    for _ in range(corridas):
        r = random.random()
        x = -ex*math.log(r)
        resultados.append(x)
    return resultados



def gamma(k, a, n_corridas):
    valores_aleatorios = []
    for _ in range(n_corridas):
        tr = 1.0
        for _ in range(k):
            r = random.random()
            tr *= r
        x = -math.log(tr) / a
        valores_aleatorios.append(x)
    return valores_aleatorios


def pascal_discreta(k, q):
    tr = 1.0
    qr = math.log(1 - q)  # Usamos 1 - q porque q es la probabilidad de éxito
    nx = 0
    for _ in range(k):
        r = random.random()
        tr *= r
        nx += math.log(r)  # Acumulamos el logaritmo de r para cada ensayo
    x = math.ceil(nx / qr)  # Usamos ceil para obtener el valor entero más próximo por arriba
    return x

def hypegeo_multiple(tn, ns, p, corridas):
    resultados = []
    for _ in range(corridas):
        x = 0.0
        tn_temp = tn  # Creamos una copia de tn para no modificar el valor original
        p_temp = p  # Creamos una copia de p para no modificar el valor original
        for i in range(ns):
            r = random.random()
            if r < p_temp:
                s = 1.0
                x += 1.0
            else:
                s = 0.0
            p_temp = (tn_temp * p_temp - s) / (tn_temp - 1.0)
            tn_temp -= 1.0
        resultados.append(x)
    return resultados

# Ejemplo de uso

corridas = 1000  # Número de corridas a realizar

#POISSON
p = 3.0  # Parámetro de la distribución de Poisson
valores_aleatorios = poisson(p, corridas)

#UNIFORME
a=0
b=1
valores_uniformes = [uniform(a, b) for _ in range(corridas)]

#BINOMIAL
n = 10  # Número de ensayos
p = 0.5  # Probabilidad de éxito en cada ensayo
valores_aleatorios = binomial_distribution(n, p, corridas)

#EXPONENCIAL
ex = 0.1
valores_exponenciales = expent(ex, corridas)

#GAMMA
k = 3  # Este es el parámetro 'k' de la distribución gamma
a = 2.0  # Este es el parámetro 'a' de la distribución gamma
valores_gamma = gamma(k, a,corridas)


#PASCAL
K = 5
Q = 0.5  # Probabilidad de éxito
valores_pascal = [pascal_discreta(K, Q) for _ in range(10000)]

