from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def model_pre(image_path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(image_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    model = load_model('models/keras_model.h5')
    prediction = model.predict(data)

    className = ['여자', '남자']
    print('prediction==>', className[np.argmax(prediction)])
    return className[np.argmax(prediction)]