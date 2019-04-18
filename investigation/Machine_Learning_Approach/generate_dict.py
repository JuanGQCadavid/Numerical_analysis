import sys
import mido
import audiolazy
from mido import MidiFile
from audiolazy import lazy_midi
from audiolazy.lazy_midi import midi2freq


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

def main_code(song):
    
    """ Método main, se encarga del manejo de las canciones que se quieren leer, usando
    los métodos anteriores para la creación de un dict con los puntos (tiempo vs frecuencia) 
    de los archivos midi leídos"""
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
                            #print(str(tiempo_acumulado)+ " " + str(nota))
                            agregar_a_arreglo(tiempo_acumulado, nota)
                            last_time = tiempo_acumulado

    #print(puntos)
    return puntos

def getDic(path):
    return main_code(path)
