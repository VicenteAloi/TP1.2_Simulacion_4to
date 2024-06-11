import random
import matplotlib.pyplot as plt
from pruebas import Tests

#Convertidor de numeros generados a secuencia de binario
def converterBinary(generator):
    secuence=''
    for numgen in generator:
        if(numgen<1):
            numgen=numgen*(10**8)
        integer_part = int(numgen)
        secuence= secuence + format(integer_part,'b')
    return secuence


#Generador de Numeros Método GCL
class CongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

# Ejemplo de uso
if __name__ == "__main__":
    # Parámetros del generador congruencial lineal
    seed = 1234
    a = 1664525
    c = 1013904223
    m = 2**16
    genGCL=[]
    numGCL = []
    # Crear el generador
    generator = CongruentialGenerator(seed, a, c, m)
    # Generar algunos números pseudoaleatorios
    for i in range(0,8000):
        genGCL.append(generator.generate())
        numGCL.append(i)

#Generador de Numeros Método Random
random.seed()
gen=[]
num=[]
for i in range(0,8000):
    gen.append(random.random())
    num.append(i)


#Generador de numeros Métodos X2 de Von Neumann
def von_neumann(seed, iterations):
    numbers = []
    current_seed = seed
    
    for _ in range(iterations):
        # Square the current seed
        squared = current_seed ** 2
        
        # Convert the squared number to a string
        squared_str = str(squared)
        
        # Ensure the squared number has an even length
        if len(squared_str) % 2 != 0:
            squared_str = '0' + squared_str
        
        # Extract the middle digits
        middle_index = len(squared_str) // 2
        middle_digits = squared_str[middle_index - 3: middle_index + 3]
        
        # Convert the middle digits back to an integer
        next_seed = int(middle_digits)
        
        # Update the seed for the next iteration
        current_seed = next_seed
        
        # Normalize the generated number to be within [0, 1]
        normalized_number = next_seed / 100
        
        numbers.append(normalized_number)
    
    return numbers

# Ejemplo de uso
seed = 8979
iterations = 8000
numX=[]
for i in range(iterations):
    numX.append(i)
genX2 = von_neumann(seed, iterations)


#Convertir de Float a Binario
bGen=converterBinary(gen)
bGenGCL=converterBinary(genGCL)
bGenX2=converterBinary(genX2)

#Correr Runs Test
print('RUN TEST - Alpha=0.01')
print('Random')
p_value = Tests.runs_test(bGen)
print(p_value,Tests.interpret_p_value(p_value))
print('GCL')
p_value = Tests.runs_test(bGenGCL)
print(p_value,Tests.interpret_p_value(p_value))
print('Von Neumann')
p_value = Tests.runs_test(bGenX2)
print(p_value,Tests.interpret_p_value(p_value))

#Correr Block Frecuency Test
print('Block Frecuency Test - Alpha=0.01')
print('Random')
p_value = Tests.block_frequency_test(bGen)
print(p_value,Tests.interpret_p_value(p_value))
print('GCL')
p_value = Tests.block_frequency_test(bGenGCL)
print(p_value,Tests.interpret_p_value(p_value))
print('Von Neumann')
p_value = Tests.block_frequency_test(bGenX2)
print(p_value,Tests.interpret_p_value(p_value))

#Correr Monobit Test
print('Monobit Test - Alpha=0.01')
print('Random')
p_value = Tests.monobit_test(bGen)
print(p_value,Tests.interpret_p_value(p_value))
print('GCL')
p_value = Tests.monobit_test(bGenGCL)
print(p_value,Tests.interpret_p_value(p_value))
print('Von Neumann')
p_value = Tests.monobit_test(bGenX2)
print(p_value,Tests.interpret_p_value(p_value))

fig, ax = plt.subplots(3,figsize=(10,16))
ax[0].scatter(gen,num, c='black',s=1)
ax[1].scatter(genGCL,numGCL, c='black',s=1)
ax[2].scatter(genX2,numX, c='black',s=2)
plt.show()





