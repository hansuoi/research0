import tensorflow as tf
from tensorflow.keras.datasets import mnist
import autokeras as ak
from tensorflow.keras.utils import plot_model




(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train[:100]
y_train = y_train[:100]
x_test  = x_test[:10]
y_test  = y_test[:10]

clf = ak.ImageClassifier(max_trials=1)
clf.fit(x_train, y_train, epochs=1)

print(clf.evaluate(x_test, y_test))

print('model name = ', end='')
name = input()
tf.saved_model.save(clf, 'model/'+name)
