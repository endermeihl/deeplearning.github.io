import os
os.environ['KERAS_BACKEND']='theano'
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
digit=train_images[4]

plt.imshow(digit,cmap=plt.cm.binary)
plt.show()