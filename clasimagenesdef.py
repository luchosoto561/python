import os
import keras 
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mping

DATASET_PATH = "C:/Users/Usuario/Desktop/imagenescatdog"

# filtrado y eliminacion no deseados

def filter_images():
    deleted_imgs=0
    for folder_name in ("Cat", "Dog"):
        folder_path = os.path.join(DATASET_PATH, folder_name)
        for image in os.listdir(folder_path):
            img_path=os.path.join(folder_path, image)
            try:
                fobj = open(img_path, "rb")
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally: 
                fobj.close()
            if not is_jfif:
                deleted_imgs += 1
                os.remove(img_path)
    print(f"Imagenes eliminadas: {deleted_imgs}")
    
#pasamos imgagenes al mismo tamaño

plt.figure(figsize=(10, 10))

folder_path = os.path.join(DATASET_PATH, "Dog")
for i, image in enumerate(os.listdir(folder_path)[:9]):
    img_path = os.path.join(folder_path, image)
    img = mping.imread(img_path)
    ax = plt.subplot(3, 3, i+1)
    plt.imshow(img) 
    plt.title(f"Tamaño: {img.shape[:2][0]} x {img.shape[:2][1]} pixeles")
    plt.axis("off") 

image_size = (180, 180)
batch_size = 128 

train_ds = keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

#dividamos el conjunto de datos en las tres partes

temp_val_ds = keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split = 0.2,
    subset = "validation",
    seed = 1337,
    image_size = image_size,
    batch_size = batch_size,
)
val_size = int(0.5 * len(temp_val_ds))

val_ds = temp_val_ds.take(val_size)
test_ds = temp_val_ds.skip(val_size)

# arquitectura de la red neuronal

from keras import layers

input_shape= (180, 180, 3) 

fcnn_model= keras.Sequential() 

fcnn_model.add(layers.Input(shape=input_shape))

fcnn_model.add(layers.Rescaling(1.0/255))

fcnn_model.add(layers.Flatten())

#Layer 1
fcnn_model.add(layers.Dense(384, activation= 'relu'))

#Layer 2
fcnn_model.add(layers.Dense(256, activation='relu'))

#Layer 3
fcnn_model.add( layers.Dense(128, activation= 'relu'))

#Layer 4
fcnn_model.add(layers.Dense(1, activation='sigmoid')) 

#configuracion de la red neuronal

fcnn_model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.Adam(1e-3), metrics=['accuracy'])

#entrenamiento

history = fcnn_model.fit(train_ds, epochs=25, validation_data=val_ds)

#almacenamiento del modelo
fcnn_model.save("C:\\Users\\Usuario\\Desktop\\progra ia(2024).keras")
