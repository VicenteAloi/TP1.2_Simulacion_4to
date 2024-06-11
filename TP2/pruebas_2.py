import random
import math

#UNIFORME A POISSON
def poisson(u, lambd):
    return -math.log(1 - u) / lambd

def g_poisson_sequence(size, lambd):
    poisson_sequence = []
    for _ in range(size):
        u = random.random()  # Generar número aleatorio uniforme
        poisson_value = poisson(u, lambd)  # Convertir a distribución de Poisson
        poisson_sequence.append(poisson_value)
    return poisson_sequence

# Ejemplo de uso
lambda_value = 5  # Parámetro lambda de la distribución de Poisson
sequence_size = 10  # Tamaño de la secuencia
poisson_sequence = g_poisson_sequence(sequence_size, lambda_value)
print("Secuencia de Poisson:", poisson_sequence)

#UNIFORME A NORMAL
def normal(u1, u2, mu=0, sigma=1):
    z1 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z2 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    x1 = mu + z1 * sigma
    x2 = mu + z2 * sigma
    return x1, x2

def generate_normal_sequence(size, mu=0, sigma=1):
    normal_sequence = []
    for _ in range(size // 2):
        u1, u2 = random.random(), random.random()
        x1, x2 = normal(u1, u2, mu, sigma)
        normal_sequence.extend([x1, x2])
    return normal_sequence

# Ejemplo de uso
mu_value = 10  # Media de la distribución normal
sigma_value = 2  # Desviación estándar de la distribución normal
sequence_size = 10  # Tamaño de la secuencia (debe ser par)
normal_sequence = generate_normal_sequence(sequence_size, mu_value, sigma_value)
print("Secuencia de números aleatorios con distribución normal:", normal_sequence)
