import generate_dict as midi_song
import matplotlib.pyplot as plt

import sys

#Machine Leaning.
from sklearn import linear_model
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Perceptron


def main():

    midi_format = sys.argv[1]
    midi_dic = midi_song.getDic(midi_format)
    
    x_data = []
    y_data = []

    
    for key in midi_dic.keys():
        y_data.append(key)
        x_data.append(midi_dic[key])
        #print("Key-> ",key," Element -> ", midi_dic[key])
    

    #x_data = np.array(midi_dic.values())
    print(len(y_data))
    print(len(x_data))
    #y_data = midi_dic.keys()

    x_data = np.array(x_data)
    x_data = x_data.reshape(-1,1)

    y_data = np.array(y_data)

    #linearR(x_data,y_data)
    polinomical(x_data,y_data)
    
def ridge(x_data, y_data):
    reg = linear_model.LassoLars(alpha=.1)
    reg.fit(x_data,y_data)

    y_predicte = reg.predict(x_data)

    graph_midi(x_data,y_data,y_predicte)

def polinomical(x_data,y_data):
    #X = PolynomialFeatures(interaction_only=True).fit_transform(X)

    model = Pipeline([('poly', PolynomialFeatures(degree=20)),
                  ('linear', linear_model.LinearRegression(fit_intercept=False))])
    model.fit(x_data,y_data)
    y_predicte = model.predict(x_data)
    graph_midi(x_data,y_data,y_predicte)


def linearR(x_data,y_data):
    linear_regression = linear_model.LinearRegression()
    linear_regression.fit(x_data,y_data);

    y_predicte = linear_regression.predict(x_data)

    graph_midi(x_data,y_data,y_predicte)


def graph_midi(x_data,y_data,y_predicte):

    x_min,x_max = min(x_data), max(x_data)
    y_min,y_max = min(y_data), max(y_data)

    plt.plot(y_data, x_data,'b-', y_predicte,x_data,'r' )
    plt.axis([y_min,y_max,x_min,x_max])
    plt.show()

if __name__ == '__main__':
    main()

