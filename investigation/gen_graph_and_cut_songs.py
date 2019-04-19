import sys
import mido
import audiolazy
from mido import MidiFile
from audiolazy import lazy_midi
from audiolazy.lazy_midi import midi2freq
import matplotlib.pyplot as plt
import random

"""
In this document, I am going to use the JJ's code to generate the dict, graph it
and create a cut method that randomly delete part of the dict to simulate
lost of characteristics in a song.
"""

def get_nota(msg):
    """ Método lee el texto producido por el mensaje de conversión del Midi
    y devuelve el campo correspondiente a la nota """
    texto = str(msg)
    pos_nota = texto.find('note', 10)
    if texto[pos_nota + 7] != ' ':
        nota = texto[pos_nota+5] + texto[pos_nota+6] + texto[pos_nota+7]
    else:
        nota = texto[pos_nota+5] + texto[pos_nota+6]

    if nota.isdigit():
        nota = midi2freq(int(nota))
        return nota
    else:
        return 0


def get_vel(msg):
    """ Método lee el texto producido por el mensaje de conversión del Midi
    y devuelve el campo correspondiente a la velocidad """
    vel = 0
    texto = str(msg)
    pos_vel = texto.find('velocity', 10)
    vel = texto[pos_vel+9]
    return vel

def control(msg):
    """ Método dice si el mensaje de conversión que se está leyendo es un 
    mensaje de control o un mensaje de contenido """
    texto = str(msg)
    if 'key_signature' in texto:
        return True
    elif 'program_change' in texto:
        return True
    elif 'control_change' in texto:
        return True
    elif 'end_of_track' in texto:
        return True
    elif 'time_signature' in texto:
        return True
    else:
        return False



puntos = {}
def agregar_a_arreglo(x, y):
    puntos[x] = y

times = []
frecuencies = []
# Evinracher's code
def graph_dict(points):
    plt.plot(range(len(points)), list(points.values()))
    # Label the x axis with the time points
    plt.xticks(range(len(points)), list(points.keys()))
    plt.xlabel("Time")
    plt.ylabel("Frecuency")
    plt.show()
    
def graph_arrays(X,Y, title):
    fig = plt.subplot()
    fig.plot(X,Y, label = title)
    fig.set_xlabel("Time")
    fig.set_ylabel("Frecuency")
    fig.legend(loc='upper center', fontsize='x-large')

# Arrays used to save the modified song to be interpolated
X_array=[]
Y_array=[]
def cut_song(n):
    """
    Modify the original song deleting points of it and save the result
    in two global arrays X_array and Y_array.
    
    Parameters
    ----------
    n: int
        The numbers of point to be deleted
    
    Returns
    -------
    random_indexes:
        indexes of points that was deleted
    """
    random_indexes = random.sample(range(0,len(times)-1),n)
    global X_array
    global Y_array 
    print(random_indexes)
    print(len(times))
    for i in range(len(times)):
        if not(i in random_indexes):
            X_array.append(times[i])
            Y_array.append(frecuencies[i])
    return random_indexes

def L(X, xk, x):
    result = 1.0
    for xi in X:
        if xi != xk:
            result *= (x - xi)/(xk - xi)
    return result

def interpolate(X,Y, x):
    y_evaluation = 0.0
    n = len(X)
    for xk in range(n):
        y_evaluation += Y[xk]*L(X, X[xk], x)
    return y_evaluation

X_repaired=[]
Y_repaired=[]
def repair_song(X):
    global X_repaired
    X_repaired = X_array.copy()
    global Y_repaired
    Y_repaired = Y_array.copy()
    for i in X:
        Y_repaired.append(interpolate(X_repaired,Y_repaired, times[i]))
        X_repaired.append(times[i])
        
def main():
    
    """ Método main, se encarga del manejo de las canciones que se quieren leer, usando
    los métodos anteriores para la creación de un dict con los puntos (tiempo vs frecuencia) 
    de los archivos midi leídos"""

    song = sys.argv[1]
    print('Transformando canción: ', song)
    
    

    tiempo_acumulado = 0
    mid = MidiFile(song)
    for i, track in enumerate(mid.tracks):
        last_time = -1
        for msg in track:
            if(not control(msg)):
                if get_vel(msg) != '0':
                    nota = get_nota(msg)
                    if nota != 0:
                        tiempo_acumulado += msg.time
                        if tiempo_acumulado != last_time:
                            # print(str(tiempo_acumulado)+ " " + str(nota))
                            agregar_a_arreglo(tiempo_acumulado, nota)
                            times.append(tiempo_acumulado)
                            frecuencies.append(nota)
                            last_time = tiempo_acumulado

    #graph_dict(puntos)
    graph_arrays(times, frecuencies, "Original song")
    x = cut_song(8)
    graph_arrays(X_array,Y_array, "Modified song")
    print(len(X_array))
    print(len(Y_array))
    plt.show()
    # MALO de acá en adelante :"V
    repair_song(x)
    graph_arrays(times, frecuencies, "Original song")
    print(times)
    print(frecuencies)
    print(X_repaired)
    print(Y_repaired)
    graph_arrays(X_repaired, Y_repaired, "Repaired song")
    plt.show()
    return puntos
    
if __name__ == '__main__':
    main()
