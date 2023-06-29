import  tensorflow as tf 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from sklearn.metrics import accuracy_score
mnist = tf.keras.datasets.mnist

(X_train_full, y_train_full), (X_test, y_test) = mnist.load_data()

X_valid, X_train = X_train_full[:5000]/255, X_train_full[5000:]/255
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

X_test = X_test/255

LAYERS = [

     tf.keras.layers.Flatten(input_shape = [28,28], name = "InputLayer"),
     tf.keras.layers.Dense(300, activation = "relu", name = "HiddenLayer1"),
     tf.keras.layers.Dense(100, activation = "relu", name = "HiddenLayer2"),
     tf.keras.layers.Dense(10, activation = "softmax", name = "OutputLayer")
]
#Model Definition
model_clf = tf.keras.models.Sequential(LAYERS)

LOSS_FUNCTION = "sparse_categorical_crossentropy"
OPTIMIZER = "SGD"
METRICS = ["accuracy"]

model_clf.compile(loss= LOSS_FUNCTION, optimizer = OPTIMIZER, metrics = METRICS)


VALIDATION = [X_valid, y_valid]
EPOCHS = 30
print(model_clf.fit(X_train, y_train, validation_data = VALIDATION, epochs = EPOCHS ))

y_prob = model_clf.predict(X_test)
y_pred = np.argmax(y_prob, axis = -1)
print(f"y_pred = {y_pred}")
model_clf.save("model.h5")
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy on test data:",accuracy)

