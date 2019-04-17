
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import random

mnist_train = pd.read_csv('mnist_train.csv')
mnist_test = pd.read_csv('mnist_test.csv')

cols = ['label']
for i in range(784):
    cols.append('px_{}'.format(i+1))
#сols = ['px_{}'.format(i+1) for i in range(784)]

mnist_train.columns = cols
mnist_test.columns = cols

train_data = mnist_train.values[:,1:]
test_data = mnist_test.values[:,1:]

train_label = mnist_train.values[:,0]
test_label = mnist_test.values[:,0]

print(train_data.shape, test_data.shape)

kn_classifier = KNeighborsClassifier(n_jobs = -1)
kn_classifier = kn_classifier.fit(train_data,train_label)

y_predict = []
for i in range(0, len(test_label)):
    test_id = i
    #plt.imshow(test_data[test_id, :].reshape(28,28), cmap="Greys")
    y_predict.append(kn_classifier.predict(test_data[test_id, :].reshape(1,784))[0])
print(len(y_predict),len(test_label))

print(accuracy_score(test_label, y_predict))
