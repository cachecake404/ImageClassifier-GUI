#Import all libraries
import numpy as np
from keras.models import Sequential 
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dropout
from keras.optimizers import Adam

imgx,imgy = 150,150 #Image Size X and Y.
btsize = 32 #Batch Size


def make_classifier():
    classifier = Sequential() #Initialize Model type.
    #Create Convolution Layer1
    classifier.add(Conv2D(32, (3,3) , activation="relu" ,input_shape=(imgx,imgy,3)))
    classifier.add(MaxPooling2D(pool_size=(2,2)))
    
    #Create Convolution Layer2
    classifier.add(Conv2D(32, (3,3) , activation="relu" ))
    classifier.add(MaxPooling2D(pool_size=(2,2)))
    
    #Create Convolution Layer3
    classifier.add(Conv2D(64, (3,3) , activation="relu" ))
    classifier.add(MaxPooling2D(pool_size=(2,2)))
    
    #Create Convolution Layer4
    classifier.add(Conv2D(64, (3,3) , activation="relu" ))
    classifier.add(MaxPooling2D(pool_size=(2,2)))
    
    #Create Flattening Layer
    classifier.add(Flatten())
    
    #Create final Fully connected Layer the real ANN.
    classifier.add(Dense(units=64,activation="relu"))
    classifier.add(Dropout(p=0.6))
    classifier.add(Dense(units=64,activation="relu"))
    classifier.add(Dense(units=64,activation="relu"))
    classifier.add(Dropout(p=0.3))
    classifier.add(Dense(units=1,activation="sigmoid"))
    
    #Compile the classifier
    optimizerz = Adam(lr=1e-3) #Specify spefic type of adam optimizer u can just pass as string but this as an object gives more customization.
    classifier.compile(optimizer=optimizerz,loss="binary_crossentropy",metrics=["accuracy"])
    
    #Return Classifier.
    return classifier



def classifier_setup(train_dir,test_dir,train_num,test_num,epoch_num=25): #Just call this.
    model = make_classifier()
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    
    test_datagen = ImageDataGenerator(rescale=1./255)
    
    train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(imgx, imgy),
            batch_size=btsize,
            class_mode='binary')
    
    
    validation_generator = test_datagen.flow_from_directory(
            test_dir,
            target_size=(imgx, imgy),
            batch_size=btsize,
            class_mode='binary')
    
    model.fit_generator(
            train_generator,
            steps_per_epoch=train_num,
            epochs=epoch_num,
            validation_data=validation_generator,
            validation_steps=test_num)
    return [model,train_generator.class_indices]

def model_predict(model,mapping,test_dir):
    pic = image.load_img(test_dir,target_size=(imgx,imgy))
    pic = image.img_to_array(pic)
    pic = np.expand_dims(pic,axis=0)
    result = model.predict(pic)
    return simplify(mapping,result[0][0])

def simplify(mapping,result):
    for i in mapping:
        if mapping[i] == result:
            key = i
            break
    return key

##classifier,mapping = classifier_setup("dataset/training_set","dataset/test_set",8000/32,2000/32,epoch_num=100)

###SAVE

#import pickle
#classifier.save("cat_dog_classifier.h5")
#k = open("mapping.pkl","wb")
#pickle.dump(obj=mapping,file=k)
#k.close()
