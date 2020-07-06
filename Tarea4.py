"""
Tarea 4 Modelos Probabilísticos de Señales y Sistemas
Jeremy Alvarado D
B40252
"""
import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
from scipy import integrate

##############################################################################
#1 Crear un esquema de modulación BPSK.
##############################################################################

#Importación de datos
datos = pd.read_csv('bits10k.csv')
bits = np.array(datos)

# Frecuencia solicitada
f = 5000 # Hz

# Período 
T = 1/f 

# Número de puntos de muestreo
pt = 50

# Muestreo por periódo
MT = np.linspace(0, T, pt)

# Onda portadora
sen = np.sin(2* np.pi * f * MT)

# Gráfica de portadora
plt.plot(MT, sen)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud de la onda portadora')
plt.title('Onda Portadora')
plt.show()

# Frecuencia para el muestreo
fm = pt/T 

#Tamaño del arreglo
N= len(bits)

# Vector de tiempo para Tx
t = np.linspace(0, N * T, N * pt)

# Creación del vector de la señal modulada
senal = np.zeros(t.shape)
    
# Modulación BPSK
for k, b in enumerate(bits):
    if b == 1:
        senal[k * pt:(k+1) * pt] = sen
    else: 
        senal[k * pt:(k+1) * pt] = -sen

# Gráfica de los primeros 10 bits modulados por BPSK
pb_1 = 0
pb_2 = 10
plt.plot(senal[pb_1 * pt:pb_2 * pt])
plt.xlabel('Tiempo (ms)')
plt.ylabel('Amplitud normalizada')
plt.title('Señal Modulada con ' + str(pb_2) + ' Periódods')
plt.show()

##############################################################################
#2 Cálculo de la Pprom de la señal modulada.
##############################################################################

# Cálculo de Pinst de la señal
Pinst = senal**2

# Cálculo de la Pprom (Implementacióon de trapz)
Pp = integrate.trapz(Pinst, t) / (N * T)
print('') 
print('La potencia promedio de la señal modulada es:', Pp)
print('')
##############################################################################
#3 Simulación de canal ruidoso con AWGN con SNR desde -2 hasta 3 dB.
##############################################################################

# Vector de SRN con los valores solicitados
v_SNR = [-2,-1,0,1,2,3] 

# Vector para BER con igual cantidad de espcios que SNR
v_BER = np.zeros(6)

# Pseudo-energía de la onda original 
Es = np.sum(sen ** 2)

# Creación del vector de bits que serán recibidos depues de la modulación
bitsRx = np.zeros(bits.shape) 

for i in range(6):  
    SNR = v_SNR[i]
    
    # Desviación estándar del ruido (El argumento es la potencia del ruido)
    sigma = np.sqrt(Pp / (10 ** (SNR / 10)))

    # Crear ruido gaussiano
    ruido = np.random.normal(0, sigma, senal.shape)
    
    # Simular el canar ruidos sumandole ruido a la señal
    Rx = senal + ruido
    
       # Gráfica de la señal ruidosa
    pb = 10
    plt.figure(2)
    plt.plot(Rx[0:pb * pt])
    plt.xlabel('Tiempo / s')
    plt.title('Conjunto de señales ruidosas para SNR (-2dB, 3dB)')
    #plt.show()
##############################################################################
#5 Demodular y decodificar la señal y hacer un conteo de la tasa de error
##############################################################################
    
    #Contéo de errores
    for k, b in enumerate(bits):
        Ep = np.sum(Rx[k * pt:(k+1) * pt] * sen)
        if Ep > Es/2:
            bitsRx[k] = 1
        else:
            bitsRx[k] = 0
    
    error = np.sum(np.abs(bits - bitsRx))
    v_BER[i] = error/(N)
    print("SNR en dB:", SNR)
    print("Número de errores:", error)
    print("Probabilidad de errores:", v_BER[i] )
    print('') 
    
##############################################################################    
#4 Gráficas de densidad espectral de potencia antes y después del canal ruidoso
##############################################################################    

# Antes de canal ruidoso
fw, PSD = signal.welch(senal,fm,nperseg=1024)
plt.figure()    
plt.grid(True)
plt.semilogy(fw, PSD)
plt.title('Densidad Espectral de Potencia Antes del Canal Ruidoso')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Densidad espectral de potencia (𝑉**2/Hz)')
plt.show()

# Después del canal ruidoso
fw, PSD = signal.welch(Rx,fm,nperseg=1024)
plt.figure()
plt.grid(True)
plt.semilogy(fw, PSD)
plt.title('Densidad Espectral de Potencia Después del Canal Ruidoso')
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia  (V**2/Hz)')
plt.show()

##############################################################################
#6 Graficar BER vs SNR
##############################################################################

plt.plot(v_SNR,v_BER, '--o',label='BPSK')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.grid(True)
plt.title('BER vs SNR')
plt.legend()
plt.show()