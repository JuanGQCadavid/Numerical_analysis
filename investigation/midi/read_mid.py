import sys
import mido
import pickle
import audiolazy
from mido import MidiFile, Message, MAX_PITCHWHEEL
from audiolazy import lazy_midi
from audiolazy.lazy_midi import midi2freq, freq2midi


def get_vel(msg):
    '''
    Devuelve la velocidad del mensaje
    '''

    vel = 0
    texto = str(msg)
    pos_vel = texto.find('velocity', 10)
    vel = texto[pos_vel+9]
    return vel


def create_txt(track, freqs, times, metas):
    '''
    Crea documentos que contienen la información de cada track del midi
    1 para las frecuencias, 1 para los tiempos y 1 para los meta mensajes
    '''

    freqs_file = open("frequencias" + str(track) + ".txt", "w+")
    times_file = open("tiempos" + str(track) + ".txt", "w+")
    metas_file = open("metamsgs" + str(track) + ".txt", "wb")

    for f in freqs:
        freqs_file.write(str(int(f)))
        freqs_file.write("\n")

    for t in times:
        times_file.write(str(t))
        times_file.write("\n")

    pickle.dump(metas, metas_file)

    freqs_file.close()
    times_file.close()
    metas_file.close()


def read_mid(song):
    '''
    Guarda 3 listas, una con las frecuencias (notas), otra con los tiempos y otra con los metamensajes de la canción
    '''

    mid = MidiFile(song)
    my_tracks = []

    
    for track in mid.tracks:
        tiempo_acumulado = 0
        last_time = -1

        frequencias = []
        tiempos = []
        meta_msgs = []
        i = 0
        for msg in track:
            if msg.type == 'note_on':

                # Velocidad = 0 es equivalente a "note_off"
                if get_vel(msg) != '0':

                    # Esto convierte el tiempo relativo a tiempo absoluto
                    tiempo_acumulado += msg.time

                    # Revisa que  no se vayan a guardar dos notas en un mismo tiempo
                    # y guarda las que son de tiempos diferentes
                    if tiempo_acumulado != last_time:
                        frequencias.append(midi2freq(msg.note))
                        tiempos.append(tiempo_acumulado)
                        last_time = tiempo_acumulado

            # Guarda meta mensajes
            else:
                meta_msgs.append(msg)


        my_tracks.append([frequencias, tiempos, meta_msgs])
        create_txt(i, frequencias, tiempos, meta_msgs)
    num_tracks_file = open("num_tracks.txt", "w+")
    num_tracks_file.write(str(i))
    num_tracks_file.close()
    print("Control files created succesfully!")

def main():
    song = sys.argv[1]
    read_mid(song)
    
if __name__ == '__main__':
    main()