import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data # mnest dataset: gathering data is tedius. use an sample 

'''
input > weight > hidden layer 1 (activation function) > weights > hidden layer 2
(activate function) > weights > output layer > 

compare output to intended output > cost function (cross entropy)
optionmize function (optimizer) > minimizor cost (AdamOptimizor ...SGD, AdaGrad)

backpropagation

feed forward + backprop = epoch
'''

mnist = input_data.read_data_sets('/tmp/data/', one_hot=True) # one is on and other is off
# 10 classes, 0-9
'''
0 = [1,0,0,0,0,0,0,0,0,0]
1 = [0,1,0,0,0,0,0,0,0,0]
2 = [0,0,1,0,0,0,0,0,0,0]
3 = [0,0,0,1,0,0,0,0,0,0]
...
'''
n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 10
batch_size = 100
 
x = tf.placeholder('float', [None, 784]) # input data [height, width]
y = tf.placeholder('float') 

def neural_network_model(data):
    
    hidden_1_layer = {
        'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))
        # added in after the weights, some nerual also fires after weights. ...why?
    }
    hidden_2_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl2])), # 앞은 어떤 값이 되어도 괜찮음
        'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))
    }
    hidden_3_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
        'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))
    }
    output_layer = {
        'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
        'biases': tf.Variable(tf.random_normal([n_classes]))
    }

    # (input_data * weights) + biases

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights'])+hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1) # optimization function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights'])+hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l2 = tf.add(tf.matmul(l2, hidden_3_layer['weights'])+hidden_3_layer['biases'])
    l2 = tf.nn.relu(l3)

    output = tf.add(tf.matmul(l3, output_layer['weights'])+output_layer['biases'])

    return output

