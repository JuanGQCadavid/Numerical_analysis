"""
This script reads a song in midi format, generate a list of points that 
represent the song, plot it and modify the list by deleting some points
simulating lost of characteristics in a song. Then tries to recover the
some using interpolation and plot the result.

Created on Apr 2019

@autor: Lucumi's Followers
TODO: Translate to English all code
"""

import sys
from mido import MidiFile
from audiolazy.lazy_midi import midi2freq
import matplotlib.pyplot as plt
import random

# Dict used to save the original song
points = {}
# Arrays used to save the original song
times = []
frecuencies = []
# Arrays used to save the modified song to be interpolated
X_array=[]
Y_array=[]
# Arrays used to save the repaired song
X_repaired=[]
Y_repaired=[]


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

def agregar_a_arreglo(x, y):
    points[x] = y


# Evinracher's code
def graph_dict(points):
    """Plot the song represented by a dict of points (X,Y)
    
    Parameters
    ----------
    
    points : dict
        The dict that contains the points (X,Y) to plot
    """
    
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

def cut_song(n, random_type):
    """Modify the original song deleting points of it and save the result
    in two global arrays X_array and Y_array.
    
    Parameters
    ----------
    n : integer
        The numbers of point to be deleted
    random : bool
        Is True if you want generated a random list of X values
    
    Returns
    -------
    indexes : list
        indexes of points that was deleted
    """
    global X_array
    global Y_array 
    indexes =[]
    
    if random_type == False:
        indexes = [2, 11, 3, 23, 13, 5, 14, 16, 18, 17]
    else:
        indexes = random.sample(range(0,len(times)-1),n)
    print("Deleting the values in these indixes: ",indexes)   
    indexes.sort()
 
    for i in range(len(times)):
        if not(i in indexes):
            X_array.append(times[i])
            Y_array.append(frecuencies[i])
    return indexes

def L(X, xk, x):
    result = 1.0
    for xi in X:
        if xi != xk:
            result *= (x - xi)/(xk - xi)
    return result

def interpolate_by_lagrange(X,Y, x):
    y_evaluation = 0.0
    n = len(X)
    for xk in range(n):
        y_evaluation += Y[xk]*L(X, X[xk], x)
    return y_evaluation

def interpolate_by_neville(X,Px,x):
    n = len(X)
    matriz = [None] * n
    for i in range(n):
        matriz[i] = [None] * n
    for i in range(n):
        matriz[0][i] = Px[i]

    for grado in range(1,n):
        j = grado
        for i in range(0, n-grado):
            Pi = matriz[grado-1][j-1]
            Pj = matriz[grado-1][j]
            matriz[grado][j] = ((x-X[i])*Pj-(x-X[j])*Pi)/(X[j]-X[i])
            j += 1
    return matriz[n-1][n-1]

def repair_song_interpolating(X, interpolation_type):
    """Get the repaired song and save it into X_repaired and Y_repaired lists
    
    This method can use two types of interpolations for generated the repaired
    song: lagrange and neville
    
    Parameters
    ----------
    X : list
        A list of indexes of times list that will be the x values for each
        interpolation
    interpolation_type : str
        A string with the name of the interpolation. It can take either "lagrange"
        or "neville" as value
    
    Raises
    ------
    ValueError
        if interpolation type isn't an implemented interpolation method    
    """
    global X_repaired
    X_repaired = X_array.copy()
    global Y_repaired
    Y_repaired = Y_array.copy()
    for i in X:
        if(interpolation_type == "lagrange"):
            Y_repaired.append(interpolate_by_lagrange(X_repaired,Y_repaired, times[i]))
        elif(interpolation_type== "neville"):
            Y_repaired.append(interpolate_by_neville(X_array,Y_array, times[i]))
        else:
            Ex = ValueError()
            Ex.strerror = str("Interpolation method unknown: " + interpolation_type)
            raise Ex
        X_repaired.append(times[i])
    print("Repairing by interpolation using",interpolation_type, "method")
    

def order_song(X,Y):
    f_dict ={}
    for i in range(len(X)):
        f_dict[X[i]] = Y[i]
    X.sort()
    for i in range(len(X)):
        Y[i] = f_dict[X[i]]
        
def main():
    
    """ Método main, se encarga del manejo de las canciones que se quieren leer, usando
    los métodos anteriores para la creación de un dict con los puntos (tiempo vs frecuencia) 
    de los archivos midi leídos"""

    song = sys.argv[1]
    print("Transforming song: ", song)
      
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

    #graph_dict(points)
    graph_arrays(times, frecuencies, "Original song")
    x = cut_song(10, False)
    graph_arrays(X_array,Y_array, "Modified song")
    plt.show()
    try:
        repair_song_interpolating(x, "lagrange")
        graph_arrays(times, frecuencies, "Original song")
        order_song(X_repaired, Y_repaired)
        graph_arrays(X_repaired, Y_repaired, "Repaired song")
        plt.show()
    except ValueError as e:
        print("ValueError Exception! ", e.strerror)
    return points
    
if __name__ == '__main__':
    main()
