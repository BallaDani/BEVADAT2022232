import tensorflow as tf
import numpy as np

def cifar100_data():
    (train_images,train_labels),(test_images,test_labels)=tf.keras.datasets.cifar100.load_data()
    train_images=train_images/255.0
    test_images=test_images/255.0
    return train_images, train_labels,test_images,test_labels



def cifar100_model():
    model=tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32,(3,3), activation="softmax",input_shape=(32, 32, 3)))
    model.add(tf.keras.layers.MaxPool2D((2,2)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64, activation='softmax'))
    model.add(tf.keras.layers.Dense(10))
    return model

def model_compile(model):
    compiled=model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
    return compiled

def model_fit(model,epochs,train_images,train_labels, ):
    return model.fit(train_images, train_labels, epochs=epochs)

def model_evaluate(model, test_images, test_labels):

    test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
    return test_loss,test_acc