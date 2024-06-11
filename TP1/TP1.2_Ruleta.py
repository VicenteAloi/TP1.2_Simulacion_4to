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

frec_abs_elegido = []
frec_rel_elegido = []


#Validaciones de entrada
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


#Definicion de Estrategias
def martingala():
    rdo_tiradas = []
    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        frec_abs_elegido.append(0)
        frec_rel_elegido.append([0.0])
        apuesta_min_m=apuesta_min
        
        #Validamos Tipo Capital 
        if(tipo_capital=='f'): 
          capital.append([5000])
        else:
           capital.append([0])


        for i in range(1,len(x)):      
              #Genera numero Random y lo guarada en arreglo
              rdo_tiradas[j].append(random.randint(0,36)) 
              #Si el resultado es igual al numero elegido, suma refuencia abs del mismo
              if((tipo_capital=='f' and capital[j][i-1] >= apuesta_min_m) or tipo_capital=='i'):
                frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
                if(num_elegido.__class__==int):
                  
                  if rdo_tiradas[j][i] == num_elegido:                  
                      capital[j].append(capital[j][i-1] + apuesta_min_m*35)
                      apuesta_min_m=apuesta_min    
                      frec_abs_elegido[j] += 1                 
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
                      frec_abs_elegido[j] += 1
                  else: 
                      capital[j].append(capital[j][i-1] - apuesta_min_m)
                      apuesta_min_m=apuesta_min_m*2+1
              else:
                 capital[j].append(capital[j][i-1])
                 frec_rel_elegido[j].append(frec_abs_elegido[j]/i)

def dAlambert():
    rdo_tiradas = []
    apuesta_min_d=apuesta_min
    for j in range(0,cant_corridas):
      
        rdo_tiradas.append([0.0])
        frec_abs_elegido.append(0)
        frec_rel_elegido.append([0.0])
        
        if(tipo_capital=='f'): 
          capital.append([5000])
        else:
           capital.append([0])


        for i in range(1,len(x)):            
                #genera num random y lo guarda en el array
                rdo_tiradas[j].append(random.randint(0,36)) 
                if((tipo_capital=='f' and capital[j][i-1] >= apuesta_min_d) or tipo_capital=='i'):
                  frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
                  if(num_elegido.__class__==int):
                    if rdo_tiradas[j][i] == num_elegido:                  
                        capital[j].append(capital[j][i-1] + apuesta_min_d*35)
                        apuesta_min_d=apuesta_min_d-1
                        frec_abs_elegido[j] += 1
                    else: 
                        capital[j].append(capital[j][i-1] - apuesta_min_d)
                        apuesta_min_d=apuesta_min_d+1
                        
                  else:
                    if(num_elegido=='r'):
                      elegido=rojo
                    else: 
                      elegido=negro
                    if rdo_tiradas[j][i] in elegido: 
                        capital[j].append(capital[j][i-1] + apuesta_min_d)
                        apuesta_min_d=apuesta_min_d-1
                        frec_abs_elegido[j] += 1
                    else: 
                        capital[j].append(capital[j][i-1] - apuesta_min_d)
                        apuesta_min_d=apuesta_min_d+1
                       
                else:
                  capital[j].append(capital[j][i-1]) 
                  frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
              
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
    #Cuando ganas duplicas la apuesta, cuando perdes volves a la inicial
    rdo_tiradas = []
    apuesta_min=1
    Act=1
    Ant=0

    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        frec_abs_elegido.append(0)
        frec_rel_elegido.append([0.0])
        if(tipo_capital=='f'): 
          capital.append([5000])
        else:
           capital.append([0])


        for i in range(1,len(x)):
            #genera num random y lo guarda en el array
            rdo_tiradas[j].append(random.randint(0,36))
            if((tipo_capital=='f' and capital[j][i-1] >= apuesta_min) or tipo_capital=='i'):
              frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
              if(num_elegido.__class__ == int):
                if (rdo_tiradas[j][i] == num_elegido): 
                      capital[j].append(capital[j][i-1]+apuesta_min*35) 
                      apuesta_min, Ant, Act = asignarApuestaF(apuesta_min, Ant, Act,True)
                      frec_abs_elegido[j] += 1
                elif(rdo_tiradas[j][i] != num_elegido): 
                    capital[j].append(capital[j][i-1]-apuesta_min) 
                    apuesta_min, Ant, Act =asignarApuestaF(apuesta_min, Ant, Act,False)
                    
              else:
                  if(num_elegido=='r'):
                    elegido=rojo
                  else:
                    elegido=negro
                  if (rdo_tiradas[j][i] in elegido): 
                    capital[j].append(capital[j][i-1]+apuesta_min) 
                    frec_abs_elegido[j] += 1
                    if(Act!=1 and Ant!=0):
                      apuesta_min, Ant, Act =asignarApuestaF(apuesta_min, Ant, Act,True)     
                  elif(rdo_tiradas[j][i] not in elegido): 
                    capital[j].append(capital[j][i-1]-apuesta_min)
                    
                    apuesta_min, Ant, Act =asignarApuestaF(apuesta_min, Ant, Act,False)                        
            else:
               capital[j].append(capital[j][i-1])
               frec_rel_elegido[j].append(frec_abs_elegido[j]/i)           

def oscarsGrind():
    #Cuando ganas duplicas la apuesta, cuando perdes volves a la inicial
    rdo_tiradas = []
    apuesta_min_o=apuesta_min

    for j in range(0,cant_corridas):
        rdo_tiradas.append([0.0])
        frec_abs_elegido.append(0)
        frec_rel_elegido.append([0.0])
        if(tipo_capital=='f'):
          capital.append([5000])
        else:
           capital.append([0])
        

        for i in range(1,len(x)):

            #genera num random y lo guarda en el array
            rdo_tiradas[j].append(random.randint(0,36))
            #si el resultado es igual al numero elegido, suma refuencia abs del mismo
            if((tipo_capital=='f' and capital[j][i-1] >= apuesta_min_o) or tipo_capital=='i'):
              frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
              if(num_elegido.__class__ == int):
                if (rdo_tiradas[j][i] == num_elegido): 
                      capital[j].append(capital[j][i-1] + apuesta_min_o*35)
                      apuesta_min_o=apuesta_min_o*2
                      frec_abs_elegido[j] += 1
                else: 
                    capital[j].append(capital[j][i-1] - apuesta_min_o) 
                    apuesta_min_o=apuesta_min
                   
              else:
                  if(num_elegido=='r'):
                    elegido=rojo
                  else:
                    elegido=negro
                  if (rdo_tiradas[j][i] in elegido): 
                    capital[j].append(capital[j][i-1] + apuesta_min_o) 
                    apuesta_min_o=apuesta_min_o*2
                    frec_abs_elegido[j] += 1
                  else: 
                    capital[j].append(capital[j][i-1]-apuesta_min_o) 
                    apuesta_min_o=apuesta_min
                  
            else:
               capital[j].append(capital[j][i-1])
               frec_rel_elegido[j].append(frec_abs_elegido[j]/i)
              

if(estrategia=='m'):
  martingala()
elif(estrategia=='d'):
  dAlambert()
elif(estrategia=='f'):
  fibonacci()
elif(estrategia=='o'):
  oscarsGrind()

fig, axs1 = plt.subplots(2,2,figsize=(10,6))
nGrafica = random.randint(0,cant_corridas-1)

#Grafica Frecuencia Relativa

if(num_elegido=='r'): 
  axs1[0][0].axhline(18/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
  axs1[0][0].bar(x,frec_rel_elegido[nGrafica],color='red',label='Frecuencia Relativa Real')
elif(num_elegido=='n'):
  axs1[0][0].axhline(18/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
  axs1[0][0].bar(x,frec_rel_elegido[nGrafica],color='black',label='Frecuencia Relativa Real')
else:
  axs1[0][0].axhline(1/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
  axs1[0][0].bar(x,frec_rel_elegido[nGrafica],color='green',label='Frecuencia Relativa Real')
axs1[0][0].legend(loc='upper right')


axs1[0][0].set_title('Frecuencia relativa Corrida: '+str(nGrafica+1))
axs1[0][0].set_xlabel('Num tiradas')
axs1[0][0].set_ylabel('frecuencia relativa')

#Grafica Capital
if(tipo_capital=='f'):
  axs1[1][0].axhline(5000, color='red', linestyle='--', linewidth=1, label='Capital inicial')
else:
  axs1[1][0].axhline(0, color='red', linestyle='--', linewidth=1, label='Capital inicial')
axs1[1][0].plot(x,capital[nGrafica])
axs1[1][0].set_title('Flujo de Capital Corrida: '+str(nGrafica+1))
axs1[1][0].set_xlabel('Num tiradas')
axs1[1][0].set_ylabel('Cantidad de capital')


# fig2, axs2 = plt.subplots(2, figsize=(10,6))
for i in range(0,cant_corridas):
    if(num_elegido=='r'): 
      axs1[0][1].axhline(18/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
      axs1[0][1].bar(x,frec_rel_elegido[i],label='Frecuencia Relativa Real')
    elif(num_elegido=='n'):
      axs1[0][1].axhline(18/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
      axs1[0][1].bar(x,frec_rel_elegido[i],label='Frecuencia Relativa Real')
    else:
      axs1[0][1].axhline(1/37, color='blue', linestyle='--', linewidth=1, label='Frecuencia Relativa Esperada')
      axs1[0][1].bar(x,frec_rel_elegido[i],label='Frecuencia Relativa Real')
    axs1[0][1].set_title('Frecuencia Relativa Total')
    axs1[0][1].set_xlabel('Num tiradas')
    axs1[0][1].set_ylabel('frecuencia relativa')
    # axs1[0][1].fill(False)
    if(tipo_capital=='f'):
      axs1[1][1].axhline(5000, color='red', linestyle='--', linewidth=1, label='Capital inicial')
    else:
      axs1[1][1].axhline(0, color='red', linestyle='--', linewidth=1, label='Capital inicial')
    axs1[1][1].plot(x,capital[i])    
    axs1[1][1].set_title('Flujo de Capital Total')
    axs1[1][1].set_xlabel('Num tiradas')
    axs1[1][1].set_ylabel('Cantidad de capital')

plt.tight_layout()
plt.show()