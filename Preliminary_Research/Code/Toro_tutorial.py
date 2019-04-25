#Imports
import numpy as np



data = open('t8.shakespeare.txt','r').read()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars) #vocab_size is the number of unique characters the text contains.


char_to_ix = { ch:i for i,ch in enumerate(chars)}
ix_to_char = { i:ch for i, ch in enumerate(chars)}

print(char_to_ix)
print(ix_to_char)

import numpy as np
 
vector_for_char_a = np.zeros((vocab_size, 1))
vector_for_char_a[char_to_ix['a']] = 1
print(vector_for_char_a.ravel())


#Hyperparametres

hidden_size = 1000 #Hidden Layer size;
seq_length = 25 # Length of the input seq
learning_rate = 1e-1

#Model parameters

Wxh = np.random.randn(hidden_size, vocab_size) * 0.01
Whh = np.random.randn(hidden_size, hidden_size) * 0.01
Why = np.random.randn(vocab_size, hidden_size) * 0.01
bh = np.zeros((hidden_size, 1))
by = np.zeros((vocab_size, 1))


print(len(Wxh))
print(len(Wxh[0]))


'''



'''