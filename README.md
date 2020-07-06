# Tarea4
Presentación de los resultados obtenidos al realizar una modulación BPSK a partir de 10000 bits, con una frecuencia de 5 kHz

1) Inicialmente se presenta una forma de onda tipo senoidal, que nos permitirá funcionar como onda portadora de los bits con los que se trabajrá. 
Para la mudulación se desarrolla una sección de detección de ceros y unos indicando el cambio de estado de los bits, es decir cambiar de cero a uno implica modificación en la forma de onda del senoide. Estas gráficas se observan en la figura (Señal portadora, Señal modulada) respectivaemnte. Es importante destacar que solamente se presentan 10 periodos, para poder analizar con claridad el comportamiento de la onda ante la modulación.

2) La potencia promedio se calculo a partir de realizar la integración en el tiempo de de la potencia instantanea de la señal modulada, este proceso nos generó un valor de potencia de Pprom = 0.490 W. 

3) Para simular un canal ruidoso, fue necesario la generación aleatoria de valores con distribución gaussianos, como se solicitaba un rango de entre -3 dB hasta 2 dB, se hizo un arreglo con dichos valores que nos permitió anlaizar el comportamiento de la onda ante diferentes rangos de ruido esto se puede observar en las figuras( -2dB, -1dB, 0dB, 1dB, 2dB, 3dB) además se puede observar la distorción de la señal modulada en la figura (Conjunto de señales ruidosas), al incluir ruido a la señal modulada se distorciona la señal y por ende es difícil de interpretar la información.

4) Al graficar las densidades espectrales de potencia antes y después del canal ruidoso, es posible observar cómo está distribuida la potencia la señal sobre las distintas frecuencias de las que está formada, estos resultados se pueden observar en las figuras (Densidad de potencia antes del ruido, Densidad de potencia despues del ruido), con base en estas gráficas, es fácil deducir que inicialmente la potencia estaba perfectamente distribuiada a lo largo de las frecuencias que la formaban durante toda su duración, pero eso solo sería un caso ideal, ya que si observamos la gráfica de Densidad de potencia despues del ruido, se asemeja más a la realidad y se puede concluir que la mayor cantidad de potencia se acumula al inicio, es decir, con el paso de las frecuencias la señal pierde potencia.

5) Para demodular y decodificar la señal fue necesario calcular la potencia del ruido, que corresponde, con base en lo que ya conocemos del curso a la desviación estándar de la distribución, es por ello la importancia de obtener este parámetro en la modulación, para decodificar fue necesario determinar los cerps y unos que se reciben, con base en este desarollo es posible calcular la cantidad de errores y el BER (Parámetro importante en la modulación), para la cantidad de errores se debió detectar la presencia de ceros y unos y compararlos con la señal, al momento de que no coincidan se gereará un error. 
Dato importante: Como se genera ruido gaussiano de forma aleatoria, cada vez que se ejecuta el código, los errores serán distintos, sin embargo, todos estos resultados se obtuvieron de la ejecución que se presenta en la figura (Resultados BER vs SNR), donde se muestra que : 
 SNR = -2 -> 16 errores -> 0.0016 de probabilidad
 
 SNR = -1 -> 4 errores -> 0.0004 de probabilidad
 
 SNR = 0 -> 1 errores -> 0.0001 de probabilidad
 
 SNR = 1 -> 0 errores -> 0.0000 de probabilidad
 
 SNR = 2 -> 0 errores -> 0.0000 de probabilidad
 
 SNR = 3 -> 0 errores -> 0.0000 de probabilidad

6) La gráfica de BER vs SNR se obtiene de forma sencilla con base en los datos que se obtuvieron en lo puntos anteriores y nos indica graficamente lo que se obtuvo en el punto 5, indicando la correspondencia entre la probabilidad de error o el porcentaje de error con el valor en decibeles. Este resultado se puede observar en la figura (BER vs SNR).

