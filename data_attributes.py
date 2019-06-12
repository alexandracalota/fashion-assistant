from __future__ import print_function
from keras.datasets import mnist
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from PIL import Image
from global_vars import *

from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

import numpy as np
import pickle
import csv
import cv2
import matplotlib.pyplot as plt
import gc

def get_img_attr(file, label):
    images = []
    categories = []
    i = 0

    input_file = open(resources_path + file, "r")
    for line in input_file.readlines():
        line_list = line.split()
        if len(line_list) == 2:
            try:
                category = int(line_list[1])
                categories.append(category)

                img = cv2.imread(resources_path + line_list[0], 0)
                img = cv2.resize(img, (IMG_ROWS, IMG_COLS))

                images.append(img)

                del img

                if i % 500 == 0:
                    print('img no. ' + str(i))
                i += 1
            except ValueError:
                continue
            
    return images, categories

def cache_data(data, cache_file):
    file = open(cache_file, 'wb')
    pickle.dump(data, file)
    file.close()

def get_train_test_sets():
    print('[get_train_test]')

    images, categories = get_img_attr(attr_img_file)
    
    print('Done!')

    classes = np.unique(categories)
    nClasses = len(classes)
    
    train_data = np.array(images, dtype=np.uint8)
    del images

    print('Got train data')

    train_target = np.array(categories, dtype=np.uint8)
    del categories

    gc.collect()
    print('Got labels')

    train_data = train_data.reshape(train_data.shape[0], 1, IMG_ROWS, IMG_COLS)

    train_labels_one_hot = to_categorical(train_target)
    del train_target

    print('Reshaped data and got labels categorical')

    train_data = train_data.astype('float32')
    train_data /= 255

    train_data, test_data, train_labels, test_labels = \
        train_test_split(train_data, train_labels_one_hot, test_size=.20, random_state=42)
    del train_labels_one_hot

    cache_data((train_data, train_labels), resources_path + classes_train_data)
    cache_data((test_data, test_labels), resources_path + classes_test_data)

    return nClasses, train_data, train_labels, test_data, test_labels
