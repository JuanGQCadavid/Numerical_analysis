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

    nota = midi2freq(int(nota))

    return nota

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

def main():
    
    """ Método main, se encarga del manejo de las canciones que se quieren leer, usando
    los métodos anteriores para la creación de un dict con los puntos (tiempo vs frecuencia) 
    de los archivos midi leídos"""

    song = sys.argv[1]
    print('Transformando canción: ', song)
    
    puntos = {}
    def agregar_a_arreglo(x, y):
        puntos[x] = y

    tiempo_acumulado = 0
    mid = MidiFile(song)
    for i, track in enumerate(mid.tracks):
        last_time = -1
        for msg in track:
            if(not control(msg)):
                tiempo_acumulado += msg.time

                if get_vel(msg) != '0':
                    nota = get_nota(msg)
                    if tiempo_acumulado != last_time:
                        agregar_a_arreglo(tiempo_acumulado, nota)
                        last_time = tiempo_acumulado

    print(puntos)
    return puntos
    
if __name__ == '__main__':
    main()