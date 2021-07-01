from utils import *
from PIL import Image
import numpy as np
import tensorflow.keras.preprocessing.image
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.models import Model
import tensorflow
import h5py

preprocess_input = tensorflow.keras.applications.inception_v3.preprocess_input

encode_model=InceptionV3(weights=inception_wt_path)
encode_model=Model(encode_model.inputs,encode_model.layers[-2].output)

def encodeImage(img):
  img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
  x = tensorflow.keras.preprocessing.image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  x = encode_model.predict(x)
  x = np.reshape(x, OUTPUT_DIM )
  return x