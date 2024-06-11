from scipy.special import erfinv
import numpy as np
import matplotlib.pyplot as plt

#NORMAL
print('Normal')
def inverse_transform_sampling(n):
    # Genera n números aleatorios uniformemente distribuidos entre 0 y 1
    u = np.random.rand(n)
    
    # Función inversa de la CDF de la distribución normal estándar
    x = np.sqrt(2) * erfinv(2*u - 1)
    
    return x

# Genera 1000 muestras de la distribución normal estándar
samples = inverse_transform_sampling(1000)

# Grafica el histograma de las muestras
plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue')

# Añade una línea para la densidad de probabilidad teórica de la distribución normal estándar
x = np.linspace(-4, 4, 100)
y = (1/np.sqrt(2*np.pi)) * np.exp(-0.5*x**2)
plt.plot(x, y, color='red', linestyle='--', linewidth=2)

# Configuración del gráfico
plt.title('Histograma de muestras de la distribución normal estándar')
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.legend(['Distribución normal estándar', 'Histograma de muestras'])
plt.show()

#EXPONENCIAL
print('Exponencial')
def inverse_transform_exponential(n, lmbda):
    # Genera n números aleatorios uniformemente distribuidos entre 0 y 1
    u = np.random.rand(n)
    
    # Calcula las muestras utilizando la función inversa de la CDF de la distribución exponencial
    x = - (1 / lmbda) * np.log(1 - u)
    
    return x

# Parámetro lambda de la distribución exponencial
lmbda = 0.5

# Genera 1000 muestras de la distribución exponencial
samples = inverse_transform_exponential(1000, lmbda)

# Grafica el histograma de las muestras
plt.hist(samples, bins=30, density=True, alpha=0.7, color='green')

# Añade la función de densidad de probabilidad teórica de la distribución exponencial
x = np.linspace(0, 10, 100)
pdf = lmbda * np.exp(-lmbda * x)
plt.plot(x, pdf, color='blue', linestyle='--', linewidth=2)

# Configuración del gráfico
plt.title('Histograma de muestras de la distribución exponencial')
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.legend(['Distribución exponencial', 'Histograma de muestras'])
plt.show()


#Uniforme Continua
print('Uniforme Continua')
def inverse_transform_uniform(n, a, b):
    # Genera n números aleatorios uniformemente distribuidos entre 0 y 1
    u = np.random.rand(n)
    
    # Calcula las muestras utilizando la función inversa de la CDF de la distribución uniforme continua
    x = a + u * (b - a)
    
    return x

# Parámetros a y b de la distribución uniforme continua
a = 0
b = 10

# Genera 1000 muestras de la distribución uniforme continua
samples = inverse_transform_uniform(1000, a, b)

# Grafica el histograma de las muestras
plt.hist(samples, bins=30, density=True, alpha=0.7, color='orange')

# Configuración del gráfico
plt.title('Histograma de muestras de la distribución uniforme continua')
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.show()
