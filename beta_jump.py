#import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import seaborn as sns

np.random.seed(2)

#from sklearn.model_selection import train_test_split
#from sklearn.metrics import confusion_matrix
#import itertools

#from keras.utils.np_utils import to_categorical # convert to one-hot-encoding
#from keras.models import Sequential
#from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
#from keras.optimizers import RMSprop
#from keras.preprocessing.image import ImageDataGenerator,img_to_array
from keras.preprocessing import image
#from keras.callbacks import ReduceLROnPlateau
from keras.models import load_model

sns.set(style='white', context='notebook', palette='deep')
#import os
#import glob

class beta_jump(object):
    def __init__(self,filename):
        model = load_model('model_digtal.h5')
        model2 = load_model('model_operator.h5')
        multiplier = 16
        filename = filename
#--------------------------------------------------------------------------------
#private method        
        def compress(array,multiplier):
            small = np.zeros((28,28))
            for i in range(small.shape[0]):
                for j in range(small.shape[0]): 
                    if array[i*multiplier:(i+1)*multiplier,j*multiplier:(j+1)*multiplier].sum()>multiplier:
                        small[i,j] = 1
                    else:
                        small[i,j] = 0
            return small
        
        def predict(L):
            for i,value in enumerate(L):
                if i%2 ==0: # is even(value):
                    my_results = model.predict(value.reshape((1,28,28,1)))
                    # select the indix with the maximum probability
                    L[i] = np.argmax(my_results,axis = 1)[0]
                else:
                    my_results = model2.predict(value.reshape((1,28,28,1)))
                    # select the indix with the maximum probability
                    L[i] = np.argmax(my_results,axis = 1)[0]
            return L
        def to_expression(L):
            expression_local = ""
            for index,element in enumerate(L):
                if index %2 ==0:
                    expression_local =expression_local+ str(element)
                else:
                    if element == 0:
                        expression_local =expression_local+ "+"
                    elif element == 1:
                        expression_local =expression_local+ "-"
                    elif element == 2:
                        expression_local =expression_local+ "*"
                    elif element == 3:
                        expression_local =expression_local+ "/" 
                    else:
                        expression_local == "unable to recogize!!"
            return expression_local        
#-----------------------------------------------------------------------------        
        
        
        temp = image.load_img(filename, target_size=(28*multiplier,28*multiplier*5))
        temp = np.array(image.img_to_array(temp) )
        temp  = (temp[:,:,0]+temp[:,:,1]+temp[:,:,2])/3/255
        temp = 1-temp
        temp = temp.reshape(28*multiplier,28*multiplier*5,1)
        L = []
        for i in range(0,5):
            L.append(temp[:,(28*multiplier*i):(28*multiplier*(i+1)),0])
        L = [compress(item,multiplier) for item in L]
        
        L = predict(L)
        self.expression = to_expression(L)
        self.value = eval(self.expression)
        
    def ask(self, ask):
        if ask.lower().find("name") !=-1 or ask.lower().find("who") !=-1:
            return "My name is beta jump"
        
        elif ask.lower().find("see") !=-1:
            return self.expression
        
        elif ask.lower().find("old") !=-1:
            return "I am three years old" 
        
        elif ask.lower().find("number") !=-1 or ask.lower().find("answer") !=-1:
            temp = self.expression + "=" + str(self.value)
            return temp
        
        elif ask.lower().find("wrong") !=-1 :
            return "I am sorry! Let me try again please!"

        elif ask.lower().find("can") !=-1 :
            return "I can do math equation evaluation."
        
        elif ask.lower().find("single") !=-1 :
            return "honestly, you are not good looking~!^v^"

        elif ask.lower().find("thank") !=-1 :
            return "you are welcome!^v^"

        elif ask.lower().find("smart") !=-1 or ask.lower().find("clever") !=-1:
            return "Thank you so much! ^v^"

        elif ask.lower().find("bye") !=-1 :
            return "Have a goooood day~~! "

        elif ask.lower().find("hi") !=-1 or ask.lower().find("hello") !=-1 :
            return "Hi~~~! I'm Beta Jump "

        else:
            return "Sorry, I don't know"
        

