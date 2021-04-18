import base64
from pathlib import Path
import os

import numpy as np
import skimage.io
import skimage.transform
import skimage.color
import skimage.util
from tensorflow import keras
from keras import backend as K
from mainpage.neural.labels import label


def showpic(img):
    skimage.io.imshow(img)
    skimage.io.show()


def recognition(img):
    link = os.path.join(Path(__file__).resolve().parent, 'hiragana.h5')
    model = keras.models.load_model(link)
    model.compile(optimizer='adam',
                  loss="sparse_categorical_crossentropy",
                  metrics=['accuracy'])
    if K.image_data_format() == "channels_first":
        test_img = np.reshape(img, (-1, 1, 48, 48))
    else:
        test_img = np.reshape(img, (-1, 48, 48, 1))
    prediction = model.predict(test_img)
    classes_top3 = (np.argpartition(prediction, range(-4, 0), axis=1)[:, :-(4+1):-1]).flatten()
    hieroglyphs = [label[i] for i in classes_top3]
    result = [{'mark': hieroglyphs[i], 'prob':float(prediction[0][classes_top3[i]])} for i in range(len(classes_top3))]
    return result
    # print(result)
    # for i in classes_top3:
    #     print('mark - {0} with chance - {1}'.format(label[i], prediction[0][i]))


def decode(base64_string):
    base64_string = base64_string.split(",")[1]
    if isinstance(base64_string, bytes):
        base64_string = base64_string.decode("utf-8")

    imgdata = base64.b64decode(base64_string)
    img = skimage.io.imread(imgdata, plugin='imageio')
    img_res = skimage.transform.resize(img, (48, 48))
    img_res = skimage.color.rgb2gray(skimage.color.rgba2rgb(img_res))
    img_res = skimage.util.invert(img_res)
    return img_res


def dowork(base64_string):
    img = decode(base64_string)
    #showpic(img)
    res = recognition(img)
    return res

#dowork(test)
# TODO: КАРТИНКА ДОЛЖНА БЫТЬ ВИДА (Х,У, НАСЫШЕННОСТЬ) 0 - белый, 1 - черный