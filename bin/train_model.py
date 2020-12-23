import tensorflow as tf 
import pandas as pd 
import numpy as np 
import sklearn
import vienna_data


def construct_training_sets():
    input_data = InputData()
    train_images = input_data.training_images()
    train_labels = input_data.training_labels()
    return train_images, train_labels

def build_model():
    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape = (50, 30)),
    tf.keras.layers.Dense(350, activation=tf.nn.relu),
    tf.keras.layers.Dense(160, activation=tf.nn.softmax),
    ])
    return model

def fit_model(model, data, labels):
    mod = model.fit(train_images, 
                    train_labels,
                    validation_split=0.1,
                    epochs=30)
    return mod

def run():
    train_images, train_labels = construct_training_sets()
    mod = build_model()
    fitted_model = fit_model(mod, train_images, train_labels)
    return(fitted_model)

if __name__ == '__main__':
    run()