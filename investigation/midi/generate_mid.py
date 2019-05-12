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