#imports from Keras package
from keras.models import model_from_json
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
##
from django_website.Primitives.GeoImage import GeoImage
from matplotlib import pyplot as plt

class PoleWiresFilter(ImageFilter):
    #Based on Keras deep learning package
    filterName = "PoleWires"
    filterId = "PoleWires"

    def _initialize(cls):
        pass
    def processImage(geoImage: GeoImage):

        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model.h5")

        #test
        from keras.preprocessing import image
        #test_image = geoImage.data
        
        test_image = image.load_img(geoImage.data, target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        training_set.class_indices
        if result[0][0] == 1:
            prediction = np.ones(640, 640)
        else:
            prediction = np.ones(640, 640)
        return prediction
