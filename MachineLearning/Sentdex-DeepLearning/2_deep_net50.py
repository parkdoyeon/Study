import os
import tensorflow as tf
import pickle
import numpy as np

from deep_net48 import create_feature_sets_and_labels

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

train_x,train_y,test_x,test_y = create_feature_sets_and_labels('pos.txt', 'neg.txt')

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 2
batch_size = 100
 
x = tf.placeholder('float') # input data [height, width]
y = tf.placeholder('float') 

hidden_1_layer = {
    'weights': tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
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

def neural_network_model(data):
   
    # (input_data * weights) + biases
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']),hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1) # optimization function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']),hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']),hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output

def train_neural_network(x):
    prediction = neural_network_model(x)
    print(y)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    
    # learning_rate = 0.001
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    #cycles feed forward backprop
    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())

        for epoch in range(hm_epochs):
            epoch_loss = 0

            i = 0
            while i < len(train_x):
                start = i
                end = i+batch_size

                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x:batch_x, y:batch_y})
                epoch_loss += c
                i += batch_size
            
            print('Epoch', epoch+1, 'completed out of', hm_epochs, 'loss:', epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

        print('Accuracy:', accuracy.eval({x:test_x, y:test_y}))

train_neural_network(x)