import sys
import mido
import audiolazy
from mido import MidiFile, MidiTrack, Message, MAX_PITCHWHEEL
from audiolazy import lazy_midi
from audiolazy.lazy_midi import freq2midi


archivo = open("puntos.txt","r")

outfile = MidiFile()
track = MidiTrack()
outfile.tracks.append(track)

track.append(Message('program_change', program=12))

datos = archivo.readlines()

tiempo_anterior = 0
for x in datos:
    nota_y_tiempo = x.split()
    nota = nota_y_tiempo[1]
    nota = freq2midi(float(nota))
    
    tiempo_absoluto = nota_y_tiempo[0]
    tiempo = int(tiempo_absoluto) - int(tiempo_anterior)
    

    track.append(Message('note_on', note=int(nota), velocity=100, time=tiempo*3))
    track.append(Message('note_off', note=int(nota), velocity=100, time=10))
    tiempo_anterior = tiempo_absoluto
outfile.save('resultado.mid')

'''
import mido

mid -> Midi original.
my_tracks - > [[meta_msg],[notas_msg]]
path -> md.file_name, midi_partitures/happy.mid
def write_midi(mid,my_tracks,path):
    file = MidiFile(type=mid.type)
    file.ticks_per_beat = mid.ticks_per_beat
    for track in my_tracks:
        track_i = MidiTrack()
        #for msg in track[2]:
            #track_i.append(msg)
        
        for meta_msg in track[0]:
            track_i.append(meta_msg)
        for note in track[1]:
            track_i.append(note)
        
        file.tracks.append(track_i)
        
    file.save(path)
    print('wrote')
    
 def read_midi(mid): mid = MidiFile('midi_partitures/happy.mid')
    my_tracks = []
    for track in mid.tracks:
        meta_msg = []
        notes_msg = []
        msgs = []
        for msg in track:
            msgs.append(msg)
            if msg.type == 'note_on':
                notes_msg.append(msg)
            else:
                meta_msg.append(msg)
        
        my_tracks.append([meta_msg,notes_msg,msgs])
    
    return my_tracks
'''
