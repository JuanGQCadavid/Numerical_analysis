import generate_dict as midi_song
import matplotlib.pyplot as plt
import sys

def main():

    midi_format = sys.argv[1]
    midi_dic = midi_song.getDic(midi_format)

    for key in midi_dic.keys():
        print("Key-> ",key," Element -> ", midi_dic[key])
    
    graph_midi(midi_dic)

def graph_midi(midi_dic):

    x_data = midi_dic.values()
    y_data = midi_dic.keys()

    x_min,x_max = min(x_data), max(x_data)
    y_min,y_max = min(y_data), max(y_data)

    plt.figure(1)
    plt.plot(y_data, x_data,'b-')
    plt.axis([y_min,y_max,x_min,x_max])
    plt.show()

if __name__ == '__main__':
    main()

