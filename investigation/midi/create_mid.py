import sys
import mido
import pickle
import audiolazy
from mido import MidiFile, MidiTrack, Message
from audiolazy import lazy_midi
from audiolazy.lazy_midi import freq2midi


def create_mid(song, x):
    '''
    Recibe una lista de [frecuencias, tiempos, meta_mensajes] y la ruta del midi original
    Convierte esa información en un midi
    '''

    # Crea el archivo .mid
    original = MidiFile(song)
    mid = MidiFile(type = 1)
    mid.ticks_per_beat = original.ticks_per_beat

    archivo = open("num_tracks.txt","r")
    tracks = int(archivo.readline())

    
    for track in range(tracks+1):
        # Lee los archivos con la información necesaria para crear el mid
        freqs_file = open("frequencias" + str(track) + ".txt", "r")
        times_file = open("tiempos" + str(track) + ".txt", "r")
        metas_file = open("metamsgs" + str(track) + ".txt", "rb")

        freqs = freqs_file.readlines()
        times = times_file.readlines()
        meta_msgs = pickle.load(metas_file)
        
        track_i = MidiTrack()
        
        # Agregar los meta mensajes al track
        for meta_msg in meta_msgs:
            track_i.append(meta_msg)

        # Esperar un tiempo al inicio para que se alcance a escuchar la primera nota
        track_i.append(Message('note_on', note=60, velocity=0, time=0))
        track_i.append(Message('note_on', note=60, velocity=0, time=200))

        # Convierte de timepo absoluto a relativo
        # Agrega los mensajes de notas al track
        tiempo_anterior = 0
        for frequencia, tiempo in zip(freqs, times):
            
            tiempo_relativo = int(tiempo) - int(tiempo_anterior)
            tiempo_anterior = tiempo
            nota = int(freq2midi(int(frequencia)))

            # Acá se crean los mensajes para agregarlos al track 
            track_i.append(Message('note_on', note=nota, velocity=100, time=tiempo_relativo))

            # Este "X" es hardcoded porque no hay acceso a los mensajes que muestran el fin de una nota
            # Cada nota va a durar X ticks
            track_i.append(Message('note_on', note=nota, velocity=0, time=tiempo_relativo + x))
        
        # Esperar un tiempo al final para que se alcance a escuchar la última nota
        track_i.append(Message('note_on', note=60, velocity=0, time=200))


        mid.tracks.append(track_i)
    print("File \"result.mid\" created succesfully!")
    mid.save("result.mid")

def main():
    song = sys.argv[1]
    if len(sys.argv) <= 2:
        create_mid(song, 0)
    else:
        x = sys.argv[2]
        create_mid(song, int(x))
    
if __name__ == '__main__':
    main()