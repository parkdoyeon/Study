import tensorflow as tf
import pickle
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import getdata
lemmatizer = WordNetLemmatizer()

n_nodes_hl1 = 500
n_nodes_hl2 = 500

n_classes = 2
# 200 data, 10 epoch -> 52% accuracy
# 2000 data, 10 epoch -> 62% accuracy
# 2000 data, 15 epoch -> 63% accuracy
# 200,000 data, 15 epoch -> 74.3% accuracy
hm_data = 200000

batch_size = 32
total_batches = int(1600000/batch_size)
hm_epochs = 10

x = tf.placeholder('float')
y = tf.placeholder('float')

# 이 경우는 2 layer면 충분하고, 레이어가 늘어나면 overfitting이 일어날 수 있음.
hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([2638, n_nodes_hl1])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_classes])),
                'bias':tf.Variable(tf.random_normal([n_classes])),}

def neural_network_model(data):
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)
    output = tf.matmul(l2,output_layer['weight']) + output_layer['bias']
    return output

saver = tf.train.Saver()


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction,y) )
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        try:
			# 마지막 epoch을 읽어오도록 함
            epoch = int(open(getdata.get('tf.log'),'r').read().split('\n')[-2])+1
            print('STARTING:',epoch)
        except:
            epoch = 1

		# 텐서플로는 피드개념이 있어서 이와같은 방법을 쓰지 않아도 가능할 수 있음. 찾아보도록!
        while epoch <= hm_epochs:
            if epoch != 1:
                saver.restore(sess, getdata.get('model.ckpt'))
            epoch_loss = 1
            with open(getdata.get('lexicon-2500-2638.pickle'),'rb') as f:
                lexicon = pickle.load(f)
            with open(getdata.get('train_set_shuffled.csv'), buffering=20000, encoding='latin-1') as f:
                batch_x = []
                batch_y = []
                batches_run = 0
                for line in f:
                    label = line.split(':::')[0]
                    tweet = line.split(':::')[1]
                    current_words = word_tokenize(tweet.lower())
                    current_words = [lemmatizer.lemmatize(i) for i in current_words]

                    features = np.zeros(len(lexicon))

                    for word in current_words:
                        if word.lower() in lexicon:
                            index_value = lexicon.index(word.lower())
                            # OR DO +=1, test both
                            features[index_value] += 1
                    line_x = list(features)
                    line_y = eval(label)
                    batch_x.append(line_x)
                    batch_y.append(line_y)
                    if len(batch_x) >= batch_size: # 배치 단위가 올때마다만 텐서를 실행시킨다 
                        _, c = sess.run([optimizer, cost], feed_dict={x: np.array(batch_x),
                                                                  y: np.array(batch_y)}) #딕셔너리 형태로 feeding, 아까 선언했던 x와 y에 값을 넣어줌
                        epoch_loss += c
                        batch_x = [] # 작업 후 초기화
                        batch_y = []
                        batches_run +=1
                        print('Batch run:',batches_run,'/',total_batches,'| Epoch:',epoch,'| Batch Loss:',c,)

            saver.save(sess, getdata.get('model.ckpt'))
            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)
            with open(getdata.get('tf.log'),'a') as f:
                f.write(str(epoch)+'\n') 
            epoch +=1

# train_neural_network(x)

def test_neural_network():
    prediction = neural_network_model(x)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(hm_epochs):
            try:
                saver.restore(sess, getdata.get('model.ckpt'))
            except Exception as e:
                print(str(e))
            epoch_loss = 0
            
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        feature_sets = []
        labels = []
        counter = 0
        with open(getdata.get('processed-test-set.csv'), buffering=20000) as f:
            for line in f:
                try:
                    features = list(eval(line.split('::')[0]))
                    label = list(eval(line.split('::')[1]))
                    feature_sets.append(features)
                    labels.append(label)
                    counter += 1
                except:
                    pass
        print('Tested',counter,'samples.')
        test_x = np.array(feature_sets)
        test_y = np.array(labels)
        print('Accuracy:',  accuracy.eval({x:test_x, y:test_y}))

test_neural_network()






