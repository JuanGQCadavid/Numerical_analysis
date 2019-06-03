import sys
import mido
import audiolazy
from mido import MidiFile, MidiTrack, Message, MAX_PITCHWHEEL
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


# Esto es para guardar los meta y las notas en un archivo de texto para poder 
# desacoplar los métodos en dos archivos diferentes, uno "read_mid" y otro "create_mid"
# Luego se hace bien, por ahora todo en un mismo archivo
'''
def create_txt(track, freqs, times, metas):
    freqs_file = open("frequencias" + str(track) + ".txt", "w+")
    times_file = open("tiempos" + str(track) + ".txt", "w+")
    metas_file = open("metamsgs" + str(track) + ".txt", "w+")

    freqs_file.write(freqs)
    times_file.write(times)
    metas_file.write(metas)

    freqs_file.close()
    times_file.close()
    metas_file.close()
'''

def read_midi(song):
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
        #create_txt(i, frequencias, tiempos, meta_msg)
    return(my_tracks)



def create_mid(tracks, song):
    '''
    Recibe una lista de [frecuencias, tiempos meta_mensajes] y la ruta del midi original
    Convierte esa información en un midi
    '''

    original = MidiFile(song)
    mid = MidiFile(type = 1)
    mid.ticks_per_beat = original.ticks_per_beat

    
    for track in tracks:
        track_i = MidiTrack()
        
        # Agregar los meta mensajes al track
        for meta_msg in track[2]:
            track_i.append(meta_msg)

        # Convierte de timepo absoluto a relativo
        # Agrega los mensajes de notas al track
        tiempo_anterior = 0
        for frequencia, tiempo in zip(track[0], track[1]):
            
            tiempo_relativo = int(tiempo) - int(tiempo_anterior)
            tiempo_anterior = tiempo
            nota = int(freq2midi(frequencia))

            # Acá se crean los mensajes para agregarlos al track 
            track_i.append(Message('note_on', note=nota, velocity=100, time=tiempo_relativo))

            # Este "5" es hardcoded porque no hay acceso a los mensajes que muestran el fin de una nota
            # Cada nota va a durar 5 ticks
            track_i.append(Message('note_on', note=nota, velocity=0, time=tiempo_relativo+5))
        
        mid.tracks.append(track_i)
        
    # Estos ciclos con print son solo para ver qué es lo que se está creando
    for tr in mid.tracks:
        for ms in tr:
            print(ms)
        
    mid.save("resultado.mid")


def main():
    song = sys.argv[1]
    tracks = read_midi(song)
    create_mid(tracks, song)
    
if __name__ == '__main__':
    main()