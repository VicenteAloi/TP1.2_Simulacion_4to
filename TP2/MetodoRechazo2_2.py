import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt
import math
import random
from collections import Counter

#Uniforme Continua
print('Uniforme')
#Define la función de densidad de probabilidad (PDF) de la distribución uniforme en el intervalo dado:
def uniforme_pdf(x, a, b):
    return 1.0 / (b - a) if a <= x <= b else 0
#Define una función para generar números aleatorios que sigan una distribución uniforme en el intervalo dado:
def generar_uniforme(a, b, n):
    # Generar números aleatorios para x y y
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, 1, n)
    
    # Evaluar la PDF uniforme en x
    pdf_vals = [uniforme_pdf(val, a, b) for val in x]
    
    # Aceptar o rechazar los valores generados
    aceptados = x[y < pdf_vals]
    
    return aceptados
#Visualiza la distribución generada junto con la distribución teórica:
a = 2  # Extremo inferior del intervalo
b = 8  # Extremo superior del intervalo
n = 10000  # Número de muestras

# Generar muestras con el método de rechazo
muestras = generar_uniforme(a, b, n)

# Crear histograma de las muestras generadas
plt.hist(muestras, bins=50, density=True, alpha=0.6, color='b', label='Histograma de Muestras')

# Crear distribución uniforme teórica para comparar
x_vals = np.linspace(a, b, 100)
y_vals = [uniforme_pdf(val, a, b) for val in x_vals]
plt.plot(x_vals, y_vals, 'r--', label='Distribución Uniforme Teórica')

plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Uniforme Generada vs. Teórica')
plt.grid(True)
plt.legend()
plt.show()


#Exponencial
print('Exponencial')
#Define la función de densidad de probabilidad (PDF) de la distribución exponencial:
def expon_pdf(x, lam):
    return lam * np.exp(-lam * x)

#Define una función para generar números aleatorios que sigan una distribución exponencial:
def generar_exponencial(lam, n):
    # Generar números aleatorios para x y y
    x = np.random.uniform(0, 5/lam, n)
    y = np.random.uniform(0, lam, n)
    
    # Evaluar la PDF exponencial en x
    pdf_vals = expon_pdf(x, lam)
    
    # Aceptar o rechazar los valores generados
    aceptados = x[y < pdf_vals]
    
    return aceptados

#Visualiza la distribución generada junto con la distribución teórica:
lam = 1.0  # Parámetro de la distribución exponencial
n = 10000  # Número de muestras

# Generar muestras con el método de rechazo
muestras = generar_exponencial(lam, n)

# Crear histograma de las muestras generadas
plt.hist(muestras, bins=50, density=True, alpha=0.6, color='g', label='Histograma de Muestras')

# Crear distribución exponencial teórica para comparar
x_vals = np.linspace(0, 5/lam, 100)
y_vals = expon_pdf(x_vals, lam)

plt.plot(x_vals, y_vals, 'r--', label='Distribución Exponencial Teórica')

plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Exponencial Generada vs. Teórica')
plt.grid(True)
plt.legend()
plt.show()


#Gamma
print('Gamma')
#Define la función de densidad de probabilidad (PDF) de la distribución gamma:
def gamma_pdf(x, k, theta):
    return (x ** (k - 1) * np.exp(-x / theta)) / (theta ** k * math.gamma(k))
#Define una función para generar números aleatorios que sigan una distribución gamma:
def generar_gamma(k, theta, n):
    # Generar números aleatorios para x y y
    x = np.random.uniform(0, 20 * theta, n)
    y = np.random.uniform(0, gamma_pdf(20 * theta, k, theta), n)
    
    # Evaluar la PDF gamma en x
    pdf_vals = gamma_pdf(x, k, theta)
    
    # Aceptar o rechazar los valores generados
    aceptados = x[y < pdf_vals]
    
    return aceptados
#Visualiza la distribución generada junto con la distribución teórica:
k = 2   # Parámetro de forma
theta = 1   # Parámetro de escala
n = 10000  # Número de muestras

# Generar muestras con el método de rechazo
muestras = generar_gamma(k, theta, n)

# Crear histograma de las muestras generadas
plt.hist(muestras, bins=50, density=True, alpha=0.6, color='purple', label='Histograma de Muestras')

# Crear distribución gamma teórica para comparar
x_vals = np.linspace(0, 20 * theta, 1000)
y_vals = gamma_pdf(x_vals, k, theta)
plt.plot(x_vals, y_vals, 'r--', label='Distribución Gamma Teórica')

plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Gamma Generada vs. Teórica')
plt.grid(True)
plt.legend()
plt.show()

#Normal
print('Normal')
#Define la función de densidad de probabilidad (PDF) de la distribución normal:
def normal_pdf(x, mu, sigma):
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
#Define una función para generar números aleatorios que sigan una distribución normal:
def generar_normal(mu, sigma, n):
    # Generar números aleatorios para x y y
    x = np.random.uniform(mu - 4 * sigma, mu + 4 * sigma, n)
    y = np.random.uniform(0, normal_pdf(mu, mu, sigma), n)
    
    # Evaluar la PDF normal en x
    pdf_vals = normal_pdf(x, mu, sigma)
    
    # Aceptar o rechazar los valores generados
    aceptados = x[y < pdf_vals]
    
    return aceptados
#Visualiza la distribución generada junto con la distribución teórica:

mu = 0  # Media
sigma = 1  # Desviación estándar
n = 10000  # Número de muestras

# Generar muestras con el método de rechazo
muestras = generar_normal(mu, sigma, n)

# Crear histograma de las muestras generadas
plt.hist(muestras, bins=50, density=True, alpha=0.6, color='blue', label='Histograma de Muestras')

# Crear distribución normal teórica para comparar
x_vals = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
y_vals = normal_pdf(x_vals, mu, sigma)
plt.plot(x_vals, y_vals, 'r--', label='Distribución Normal Teórica')

plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Normal Generada vs. Teórica')
plt.grid(True)
plt.legend()
plt.show()

#Binomial
print('Binomial')
#Define la función de masa de probabilidad (PMF) de la distribución binomial:
def binomial_pmf(x, n, p):
    return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))
#Define una función para generar números aleatorios que sigan una distribución binomial:
def generar_binomial(n, p, k, m):
    # Generar números aleatorios para x y y
    x = np.random.randint(0, n + 1, m)
    y = np.random.uniform(0, binomial_pmf(n, n, p), m)
    
    # Evaluar la PMF binomial en x
    pmf_vals = binomial_pmf(x, n, p)
    
    # Aceptar o rechazar los valores generados
    aceptados = x[y < pmf_vals]
    
    # Asegurar que se generen k muestras
    while len(aceptados) < k:
        # Generar más muestras hasta obtener k muestras
        x = np.random.randint(0, n + 1, k - len(aceptados))
        y = np.random.uniform(0, binomial_pmf(n, n, p), k - len(aceptados))
        pmf_vals = binomial_pmf(x, n, p)
        aceptados = np.concatenate((aceptados, x[y < pmf_vals]))
    
    return aceptados[:k]
#Visualiza la distribución generada junto con la distribución teórica:
n = 10   # Número de ensayos
p = 0.5  # Probabilidad de éxito
k = 1000 # Número de muestras a generar
m = 10000 # Número de muestras auxiliares

# Generar muestras con el método de rechazo
muestras = generar_binomial(n, p, k, m)

# Crear histograma de las muestras generadas
plt.hist(muestras, bins=n+1, density=True, alpha=0.6, color='green', label='Histograma de Muestras')

# Crear distribución binomial teórica para comparar
x_vals = np.arange(0, n+1)
y_vals = binomial_pmf(x_vals, n, p)
plt.plot(x_vals, y_vals, 'r--', label='Distribución Binomial Teórica')

plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial Generada vs. Teórica')
plt.grid(True)
plt.legend()
plt.show()

#Poisson
print('Poisson')
def generate_poisson_samples(n_samples, mu):
    samples = []
    for _ in range(n_samples):
        total_time = 0
        events = 0
        while total_time < 1:
            time_to_next_event = np.random.exponential(1 / mu)
            total_time += time_to_next_event
            events += 1
        samples.append(events - 1)  # Restamos 1 para corregir el exceso generado por el último evento
    return np.array(samples)

# Parámetro de la distribución de Poisson (media)
mu = 5

# Generar muestras
poisson_samples = generate_poisson_samples(10000, mu)

# Histograma para visualizar las muestras generadas
plt.hist(poisson_samples, bins=30, color='pink', edgecolor='black')
plt.title('Distribución Poisson con Método de Rechazo')
plt.show()

#HiperGeometrica
print('Hipergeometrica')
def hypergeometric_pmf(k, N, K, n):
    """
    Función de masa de probabilidad (PMF) de la distribución hipergeométrica.
    """
    return math.comb(K, k) * math.comb(N - K, n - k) / math.comb(N, n)

def inverse_hypgeom_cdf(x, N, K, n):
    """
    Función de distribución acumulativa inversa (CDF inversa) de la distribución hipergeométrica.
    """
    cumulative_prob = 0
    for k in range(K + 1):
        prob = hypergeometric_pmf(k, N, K, n)
        cumulative_prob += prob
        if cumulative_prob >= x:
            return k
    return K

def uniform_to_hypergeometric(N, K, n, size):
    """
    Transformación de distribución uniforme a distribución hipergeométrica.
    """
    hypergeom_sequence = []
    for _ in range(size):
        u = random.random()  # Generar un número aleatorio uniformemente distribuido entre 0 y 1
        k = inverse_hypgeom_cdf(u, N, K, n)  # Calcular el valor correspondiente en la distribución hipergeométrica
        hypergeom_sequence.append(k)
    return hypergeom_sequence

def rejection_sampling_hypergeometric(N, K, n, size):
    """
    Genera muestras de una distribución hipergeométrica utilizando el método de rechazo.
    """
    max_pmf = max(hypergeometric_pmf(k, N, K, n) for k in range(min(n, K) + 1))
    samples = []
    while len(samples) < size:
        # Genera una muestra de la distribución binomial
        k = random.randint(0, min(n, K))
        # Genera una muestra de una distribución uniforme para aceptar o rechazar la muestra
        u = random.uniform(0, max_pmf)
        if u < hypergeometric_pmf(k, N, K, n):
            samples.append(k)
    return samples

# Parámetros de la distribución hipergeométrica
N = 100  # Tamaño de la población
K = 30   # Número total de éxitos en la población
n = 20   # Tamaño de la muestra

# Generar muestras de la distribución hipergeométrica utilizando el método de rechazo
sequence_size = 1000
hypergeom_sequence = rejection_sampling_hypergeometric(N, K, n, sequence_size)

# Calcular el rango de valores en el eje x
x_values = np.arange(min(hypergeom_sequence), max(hypergeom_sequence) + 1)

# Calcular la PMF teórica solo para los valores observados en las muestras generadas
theoretical_pmf_values = [hypergeometric_pmf(k, N, K, n) for k in x_values]
# Convertir la lista en un array numpy
theoretical_pmf_values_array = np.array(theoretical_pmf_values)
# Normalizar los valores para que sumen 1
theoretical_pmf_values_normalized = theoretical_pmf_values_array / sum(theoretical_pmf_values)

# Graficar la distribución hipergeométrica generada
plt.hist(hypergeom_sequence, bins=max(hypergeom_sequence)-min(hypergeom_sequence), color='blue', alpha=0.7, density=True, label='Muestras generadas')
# Graficar la línea teórica
plt.plot(x_values, theoretical_pmf_values_normalized, marker='o', color='red', label='PMF teórica')
plt.xlabel('Valor')
plt.ylabel('Probabilidad')
plt.title('Distribución hipergeométrica generada utilizando el método de rechazo')
plt.grid(True)
plt.legend()
plt.show()

#Pascal
print('Pascal')


# Define la PMF de la distribución de Pascal
def pascal_pmf(k, r, p):
    if k < r:
        return 0
    # Calcula el coeficiente binomial
    coef_binomial = math.factorial(k) / (math.factorial(r) * math.factorial(k - r))
    # Calcula la PMF
    return coef_binomial * (p ** r) * ((1 - p) ** (k - r))

# Define una función para generar números aleatorios que sigan una distribución de Pascal
def generar_pascal(r, p, n):
    muestras = []
    # Define el máximo valor de la PMF para el método de rechazo
    pmf_max = pascal_pmf(r + r, r, p)  # Asegúrate de que k sea al menos r
    while len(muestras) < n:
        # Genera un número aleatorio para k
        k = np.random.geometric(p) + r  # Asegúrate de que k sea al menos r
        # Genera un número aleatorio para la decisión de aceptar/rechazar
        u = random.uniform(0, pmf_max)
        # Evalúa la PMF de Pascal en k
        pmf_val = pascal_pmf(k, r, p)
        # Acepta o rechaza el valor generado
        if u < pmf_val:
            muestras.append(k)
    return muestras

# Parámetros de la distribución de Pascal
r = 3  # Número de éxitos deseados
p = 0.5  # Probabilidad de éxito en cada ensayo
n = 1000  # Número de muestras a generar

# Genera las muestras
muestras_pascal = generar_pascal(r, p, n)

def calcular_relativas(results):
  frecuencias = Counter(results)
  # Calculamos la frecuencia relativa
  frecuencia_relativa = {k: v / 10000 for k, v in frecuencias.items()}
  
  return frecuencia_relativa


# Crea el histograma de las muestras
plt.hist(muestras_pascal, bins=(max(muestras_pascal)- min(muestras_pascal)), density=True, alpha=0.6, color='blue', label='Muestras Pascal')

# Calcula y añade la línea teórica de la PMF
k_vals = np.arange(min(muestras_pascal), max(muestras_pascal) + 1)
pmf_vals = [pascal_pmf(k, r, p) for k in k_vals]
plt.plot(k_vals, pmf_vals, 'o-', color='red', label='PMF Teórica')

# Añade títulos y etiquetas
plt.title('Histograma y PMF Teórica de la Distribución de Pascal')
plt.xlabel('Número de ensayos')
plt.ylabel('Probabilidad')
plt.legend()
plt.grid(True)
# Muestra el gráfico
plt.show()