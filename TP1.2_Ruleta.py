import random
import statistics
import math
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 11 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e" or sys.argv[7] != "-s" or sys.argv[9] != "-a":
  print("Uso correcto: py TP_1.1_simulacion.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido (0 a 36)> -s <estrategia (m/d/f/o)> -a <tipo_capitañ (i/f)>")
  sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
num_elegido = sys.argv[6]
estrategia = str(sys.argv[8])
tipo_capital = str(sys.argv[10])
capital=[]
flag=False
x = list(range(0,cant_tiradas))
apuesta_min=100
rojo=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negro=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]


if(num_elegido!='r' and num_elegido!='n'):
  num_elegido=int(num_elegido)
  if(int(num_elegido)<0 and num_elegido>36):
      print("Uso correcto: py TP_1.1_simulacion.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido (0 a 36)> -s <estrategia (m/d/f/o)> -a <tipo_capitañ (i/f)>")
      sys.exit(1)


if(estrategia!='m' and estrategia!='d' and estrategia!='f' and estrategia!='o'):
  print("Uso correcto: py TP_1.1_simulacion.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido (0 a 36)> -s <estrategia (m/d/f/o)> -a <tipo_capitañ (i/f)>")
  sys.exit(1)

if(tipo_capital!='f' and tipo_capital!='i'):
  print("Uso correcto: py TP_1.1_simulacion.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido (0 a 36)> -s <estrategia (m/d/f/o)> -a <tipo_capitañ (i/f)>")
  sys.exit(1)

def martingala():
    rdo_tiradas = []
    aux_prom_tiradas = []
    prom_tiradas = []


    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        prom_tiradas.append([0.0])
        aux_prom_tiradas.append(0)
        if(tipo_capital=='f'): 
          capital.append([5000])
        else:
           capital.append([0])
        apuesta_min_m=apuesta_min
       
        for i in range(1,len(x)):      
              #Genera numero Random y lo guarada en arreglo
              rdo_tiradas[j].append(random.randint(0,36))
              print(capital[j][i-1])
              #si el resultado es igual al numero elegido, suma refuencia abs del mismo
              if((tipo_capital=='f' and capital[j][i-1] > apuesta_min_m) or tipo_capital=='i'):
                if(num_elegido.__class__==int):
                  if rdo_tiradas[j][i] == num_elegido:                  
                      capital[j].append(capital[j][i-1] + apuesta_min_m*35)
                      apuesta_min_m=apuesta_min
                  else:
                      capital[j].append(capital[j][i-1] - apuesta_min_m)
                      apuesta_min_m=apuesta_min_m*2+1
                else:
                  if(num_elegido=='r'):
                      elegido=rojo
                  else: 
                      elegido=negro
                  if rdo_tiradas[j][i] in elegido: 
                      capital[j].append(capital[j][i-1] + apuesta_min_m)
                      apuesta_min_m=apuesta_min
                  else: 
                      capital[j].append(capital[j][i-1] - apuesta_min_m)
                      apuesta_min_m=apuesta_min_m*2+1
              else:
                 print("Quebro", apuesta_min_m,capital[j][i-1])
                 capital[j].append(capital[j][i-1])
def dAlambert():
    rdo_tiradas = []
    aux_prom_tiradas = []
    prom_tiradas = []
    apuesta_min_d=apuesta_min
    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        prom_tiradas.append([0.0])
        aux_prom_tiradas.append(0)
        capital.append([50000])
        print(capital)
        for i in range(0,len(x)-1):            
                #genera num random y lo guarda en el array
                rdo_tiradas[j].append(random.randint(0,36)) 
               
                #si el resultado es igual al numero elegido, suma refuencia abs del mismo
                if(num_elegido.__class__==int):
                  if rdo_tiradas[j][i] == num_elegido:                  
                      if(i>0):
                        capital[j].append(capital[j][i] - apuesta_min_d*35)
                      apuesta_min_d=apuesta_min_d-1
                  else: 
                      if(i>0):
                        capital[j].append(capital[j][i] - apuesta_min_d)
                      apuesta_min_d=apuesta_min_d+1
                else:
                  if(num_elegido=='r'):
                     elegido=rojo
                  else: 
                     elegido=negro
                  if rdo_tiradas[j][i] in elegido: 
                      if(i>0):
                        capital[j].append(capital[j][i-1] + apuesta_min_d)
                      apuesta_min_d=apuesta_min_d-1
                  else: 
                      if(i>0):
                        capital[j].append(capital[j][i-1] - apuesta_min_d)
                      apuesta_min_d=apuesta_min_d+1
        print(capital,num_elegido)

def asignarApuestaF(apuesta_min, apuesta_min_Ant, apuesta_min_Act,flag):
      if(flag):
        apuesta_min=apuesta_min_Act-apuesta_min_Ant
        apuesta_min_Act=apuesta_min
        apuesta_min_Ant=apuesta_min_Ant-apuesta_min
      else:
        apuesta_min=apuesta_min_Act+apuesta_min_Ant
        apuesta_min_Ant = apuesta_min_Act
        apuesta_min_Act = apuesta_min
      return apuesta_min, apuesta_min_Ant, apuesta_min_Act

def fibonacci():
    rdo_tiradas = []
    aux_prom_tiradas = []
    prom_tiradas = []
    apuesta_min=1
    apuesta_min_Act=1
    apuesta_min_Ant=0
    for j in range(0,cant_corridas):

        rdo_tiradas.append([0.0])
        prom_tiradas.append([0.0])
        aux_prom_tiradas.append(0)
        capital.append([5000])
        apuesta_min=1
        apuesta_min_Act=1

        apuesta_min_Ant=0

        for i in range(0,len(x)-1):
            #genera num random y lo guarda en el array
            rdo_tiradas[j].append(random.randint(0,36))
            if((tipo_capital=='f' and capital[j][i] > apuesta_min) or tipo_capital=='i'):
              if(num_elegido.__class__ == int):
                if (rdo_tiradas[j][i] == num_elegido): 
                      capital[j].append(capital[j][i]+apuesta_min*35) 
                      apuesta_min, apuesta_min_Ant, apuesta_min_Act = asignarApuestaF(apuesta_min, apuesta_min_Ant, apuesta_min_Act,True)
                elif(rdo_tiradas[j][i] != num_elegido): 
                    capital[j].append(capital[j][i]-apuesta_min) 
                    apuesta_min, apuesta_min_Ant, apuesta_min_Act =asignarApuestaF(apuesta_min, apuesta_min_Ant, apuesta_min_Act,False)
              else:
                  if(num_elegido=='r'):
                    elegido=rojo
                  else:
                    elegido=negro
                  if (rdo_tiradas[j][i] in elegido): 
                    capital[j].append(capital[j][i]+apuesta_min) 
                    if(apuesta_min_Act!=1 and apuesta_min_Ant!=0):
                      apuesta_min, apuesta_min_Ant, apuesta_min_Act =asignarApuestaF(apuesta_min, apuesta_min_Ant, apuesta_min_Act,True)     
                  elif(rdo_tiradas[j][i] not in elegido): 
                    capital[j].append(capital[j][i]-apuesta_min)
                    apuesta_min, apuesta_min_Ant, apuesta_min_Act =asignarApuestaF(apuesta_min, apuesta_min_Ant, apuesta_min_Act,False)                        
            else:
               capital[j].append(capital[j][i])
               print("Quebro en",capital[j][i], "Apuesta minima ",apuesta_min)
        print(capital)

def oscarsGrind():
    rdo_tiradas = []
    aux_prom_tiradas = []
    prom_tiradas = []


    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        prom_tiradas.append([0.0])
        aux_prom_tiradas.append(0)
        capital.append([50000])
        apuesta_min_ini=100
        apuesta_min=apuesta_min_ini

        for i in x:
          
            #genera num random y lo guarda en el array
            rdo_tiradas[j].append(random.randint(0,36))
            #suma valores al aux promedio
            aux_prom_tiradas[j] += rdo_tiradas[j][i]
            print(apuesta_min,capital)  
            #si el resultado es igual al numero elegido, suma refuencia abs del mismo
            if(num_elegido.__class__ == int):
              if (rdo_tiradas[j][i] == num_elegido and i>0): 
                    capital[j].append(capital[j][i-1]+apuesta_min*36)               
                    apuesta_min=apuesta_min*2
                    print("gane")
              elif(rdo_tiradas[j][i] != num_elegido and i>0): 
                  capital[j].append(capital[j][i-1]-apuesta_min) 
                  apuesta_min=apuesta_min_ini
              elif(rdo_tiradas[j][i] == num_elegido and i==0):
                  capital[j].append(capital[j][i-1]+apuesta_min*36) 
                  apuesta_min=apuesta_min*2
                  print("gane")
              elif(rdo_tiradas[j][i] != num_elegido and i==0):
                  apuesta_min=apuesta_min_ini
            else:
                if(num_elegido=='r'):
                  elegido=rojo
                else:
                  elegido=negro
                if (rdo_tiradas[j][i] in elegido and i>0): 
                  capital[j].append(capital[j][i-1]+apuesta_min*2) 
                  apuesta_min=apuesta_min_ini
                  print("gane")
                elif(rdo_tiradas[j][i] not in elegido and i>0): 
                  capital[j].append(capital[j][i-1]-apuesta_min) 
                  apuesta_min=apuesta_min*2
                elif(rdo_tiradas[j][i] in elegido and i==0):
                  capital[j].append(capital[j][i-1]+apuesta_min*2) 
                  apuesta_min=apuesta_min_ini
                  print("gane")
                elif(rdo_tiradas[j][i] not in elegido and i==0):
                  apuesta_min=apuesta_min*2


if(estrategia=='m'):
   martingala()
elif(estrategia=='d'):
    dAlambert()
elif(estrategia=='f'):
   fibonacci()
elif(estrategia=='o'):
   oscarsGrind()

fig, axs1 = plt.subplots(2,figsize=(10,6))
nGrafica = random.randint(0,cant_corridas-1)

# axs1[1].axhline(0, color='black', linestyle=':',linewidth=1, label='Quiebra')
if(tipo_capital=='f'):
  axs1[1].axhline(5000, color='red', linestyle='--', linewidth=1, label='Capital inicial')
else:
  axs1[1].axhline(0, color='red', linestyle='--', linewidth=1, label='Capital inicial')
axs1[1].plot(x,capital[nGrafica])
# axs2[1].legend(loc='lower right')
axs1[1].set_title('Gráfico Flujo de Capital Corrida: '+str(nGrafica+1))
axs1[1].set_xlabel('Num tiradas')
axs1[1].set_ylabel('Cantidad de capital')

fig2, axs2 = plt.subplots(2, figsize=(10,6))
for i in range(0,cant_corridas):
    if(tipo_capital=='f'):
      axs2[1].axhline(5000, color='red', linestyle='--', linewidth=1, label='Capital inicial')
    else:
      axs2[1].axhline(0, color='red', linestyle='--', linewidth=1, label='Capital inicial')
    axs2[1].plot(x,capital[i])    
    axs2[1].set_title('Gráfico 1: Flujo de Capital')
    axs2[1].set_xlabel('Num tiradas')
    axs2[1].set_ylabel('Cantidad de capital')
    # axs2[1].set_ylim([-500000, 500000])

plt.tight_layout()
plt.show()