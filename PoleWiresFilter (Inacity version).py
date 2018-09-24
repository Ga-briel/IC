#imports from Keras package
from keras.models import model_from_json
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
##
from geojson import Point, MultiPoint, LineString, MultiLineString, Feature, FeatureCollection
from django_website.Primitives.GeoImage import GeoImage
from matplotlib import pyplot as plt
from PIL import Image

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
        entry = geoImage.data
        img = Image.fromarray(entry)
        test_image = image.load_img(img, target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        training_set.class_indices
        return result

    def processImageFromFeatureCollection(featureCollection: FeatureCollection) -> FeatureCollection:
        ##read, compile and load model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model.h5")
        ##
        """Receives a feature collection of point/line or their multi equivalents and returns a list of GeoImage's"""
        for feature in featureCollection['features']:
            if feature['geometry']['type'] == 'MultiPolygon':
                #Number of Polygons
                for polygonIndex, polygon in enumerate(feature['geometry']['coordinates']):
                    for lineIndex, lineString in enumerate(polygon):
                        for coordinateIndex in range(len(lineString)):
                            geoImage = feature['properties']['geoImages'][polygonIndex][lineIndex][coordinateIndex]
                            try:
                                geoImage = GeoImage.fromJSON(json.loads(geoImage))
                            except JSONDecodeError:
                                print('Error while parsing panorama: ' + str(geoImage)[:100]);
                                entry = geoImage.data
                                img = Image.fromarray(entry)
                                test_image = image.load_img(img, target_size = (64,64))
                                test_image = image.img_to_array(test_image)
                                test_image = np.expand_dims(test_image, axis = 0)
                                result = loaded_model.predict(test_image)
                                training_set.class_indices
                                #geoImage.processedData[GreeneryFilter.filterId] = mask
                                geoImage.setProcessedData(PoleWiresFilter.filterId, '', result)
                                feature['properties']['geoImages'][polygonIndex][lineIndex][coordinateIndex] = geoImage.toJSON()
            elif (feature['geometry']['type'] == 'MultiLineString') or (feature['geometry']['type'] == 'Polygon'):
                for lineIndex, lineString in enumerate(feature['geometry']['coordinates']):
                    for coordinateIndex in range(len(lineString)):
                        geoImage = feature['properties']['geoImages'][lineIndex][coordinateIndex]
                        try:
                            geoImage = GeoImage.fromJSON(json.loads(geoImage))
                        except JSONDecodeError:
                            print('Error while parsing panorama: ' + str(geoImage)[:100]);
                        entry = geoImage.data
                        img = Image.fromarray(entry)
                        test_image = image.load_img(img, target_size = (64,64))
                        test_image = image.img_to_array(test_image)
                        test_image = np.expand_dims(test_image, axis = 0)
                        result = loaded_model.predict(test_image)
                        training_set.class_indices
                        #geoImage.processedData[GreeneryFilter.filterId] = mask
                        geoImage.setProcessedData(PoleWiresFilter.filterId, '', result)
                        feature['properties']['geoImages'][lineIndex][coordinateIndex] = geoImage.toJSON()
            elif (feature['geometry']['type'] == 'LineString') or (feature['geometry']['type'] == 'MultiPoint'):
                for coordinateIndex in range(len(feature['geometry']['coordinates'])):
                    geoImage = feature['properties']['geoImages'][coordinateIndex]
                    try:
                        geoImage = GeoImage.fromJSON(json.loads(geoImage))
                    except JSONDecodeError:
                        print('Error while parsing panorama: ' + str(geoImage)[:100]);
                    entry = geoImage.data
                    img = Image.fromarray(entry)
                    test_image = image.load_img(img, target_size = (64,64))
                    test_image = image.img_to_array(test_image)
                    test_image = np.expand_dims(test_image, axis = 0)
                    result = loaded_model.predict(test_image)
                    training_set.class_indices
                    #geoImage.processedData[GreeneryFilter.filterId] = mask
                    geoImage.setProcessedData(PoleWiresFilter.filterId, '', result)
                    feature['properties']['geoImages'][coordinateIndex] = geoImage.toJSON()
            elif feature['geometry']['type'] == 'Point':
                coordinateIndex = 0
                geoImage = feature['properties']['geoImages'][coordinateIndex]
                try:
                    geoImage = GeoImage.fromJSON(json.loads(geoImage))
                except JSONDecodeError:
                    print('Error while parsing panorama: ' + str(geoImage)[:100]);
                entry = geoImage.data
                img = Image.fromarray(entry)
                test_image = image.load_img(img, target_size = (64,64))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis = 0)
                result = loaded_model.predict(test_image)
                training_set.class_indices
                #geoImage.processedData[GreeneryFilter.filterId] = mask
                geoImage.setProcessedData(PoleWiresFilter.filterId, '', result)
                feature['properties']['geoImages'][coordinateIndex] = geoImage.toJSON()
        return featureCollection
