#imports from Keras package
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
##
import numpy as np
#Based on Keras deep learning package
def processImage():
    classifier = Sequential()
    classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(units = 128, activation = 'relu'))
    classifier.add(Dense(units = 1, activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)
    valid_datagen = ImageDataGenerator(rescale = 1./255)
    test_datagen = ImageDataGenerator(rescale = 1./255)
    #size = 1002
    training_set = train_datagen.flow_from_directory('training_set',
    target_size = (64, 64),
    batch_size = 6,
    class_mode = 'binary')
    #size = 261
    validation_set = valid_datagen.flow_from_directory('validation_set',
    target_size = (64, 64),
    batch_size = 9,
    class_mode = 'binary')
    #size = 323
    test_set = test_datagen.flow_from_directory('test_set',
    target_size = (64, 64),
    batch_size = 19,
    class_mode = 'binary')

    classifier.fit_generator(training_set,
    steps_per_epoch = 501,
    epochs = 15,
    validation_data = validation_set,
    validation_steps = 130)

    classifier.evaluate_generator(generator=validation_set)

    #test set
    test_set.reset()
    prediction = classifier.predict_generator(test_set,verbose=1)

    #saving classifier
    model_json = classifier.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    classifier.save_weights("model.h5")
    print("Model saved")

processImage()
