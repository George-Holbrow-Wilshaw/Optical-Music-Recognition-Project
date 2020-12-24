import tensorflow as tf
import vienna_data
from sklearn.utils import shuffle

def main():

    input_data = InputData()
    train_images = input_data.training_images()
    train_labels = input_data.training_labels()
    train_images = train_images.reshape(len(train_images), 50, 30, 1)

    # Now I define the sequential keras NN and compile it
    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(3, 5, input_shape=(50, 30, 1)),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Flatten(input_shape = (50, 30, 1)),
    tf.keras.layers.Dense(800, activation=tf.nn.relu),
    tf.keras.layers.Dense(8, activation=tf.nn.softmax),
    ])

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    train_images, train_labels = shuffle(train_images, train_labels)

    model.fit(train_images, 
          train_labels,
          validation_split=0.3,
          epochs=5)

    return(model)

if __name__ == '__main__':
    main()