import tensorflow as tf 
import time
import os 

def create_model(LOSS_FUNCTION,OPTIMIZER,METRICS, no_classes):
    LAYERS = [
    tf.keras.layers.Flatten(input_shape =[28,28], name = "inputLayer"), #flatten converts 28*28 to 784 neurons
    tf.keras.layers.Dense(300, activation = "relu", name = "hiddenlayer1"),
    tf.keras.layers.Dense(100, activation  = "relu", name = "hiddenlayer2"),
    tf.keras.layers.Dense(no_classes, activation = "softmax", name = "outputLayer")]
    #Model Definition
    model_clf = tf.keras.models.Sequential(LAYERS)
    model_clf.compile(loss = LOSS_FUNCTION, optimizer = OPTIMIZER, metrics = METRICS)
    print(model_clf.summary())

    return model_clf ## untrained model

def save_model(model, model_name, model_dir):
    unique_filename = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    model.save(path_to_model)

def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S.{filename}")
    return unique_filename



