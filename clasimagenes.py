import os
#os.environ=["KERAS_BACKEND"] = "torch"

import keras 
import tensorflow as tf
import matplotlib.pyplot as plt# para que tengan las imagenes la misma resolucion
import matplotlib.image as mping

DATASET_PATH = "C:/Users/Usuario/Desktop/imagenescatdog"

# tenemos que comenzar a filtrar y eliminar las imagenes que no esten en el formato jpg

def filter_images():
    deleted_imgs=0
    for folder_name in ("Cat", "Dog"):
        folder_path = os.path.join(DATASET_PATH, folder_name)
        for image in os.listdir(folder_path):
            img_path=os.path.join(folder_path, image)
            try:
                fobj = open(img_path, "rb")
                #comprobamos si la imagen esta en formato jpg
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally: 
                fobj.close()
            if not is_jfif:
                deleted_imgs += 1
                #eliminamos la imagen correspondiente
                os.remove(img_path)
    print(f"Imagenes eliminadas: {deleted_imgs}")
    
#como todavia no tenemos todas las imagenes en el mismo tamaño todavia tenemos que adaptar las imagenes para poder darselo a una red neuronal
#en casi todos los modelos, todos los elementos de nuestro conjunto de datos tienen que ser del mismo tamaño


plt.figure(figsize=(10, 10))# defino una figura de 10 por 10

folder_path = os.path.join(DATASET_PATH, "Dog")# tengo ruta donde estan las imagenes de los perros
for i, image in enumerate(os.listdir(folder_path)[:9]):#listo los archivos de este directorio y me quedo con los primeros nueve
    img_path = os.path.join(folder_path, image)
    img = mping.imread(img_path)# lee la imagen asociada a la ruta
    ax = plt.subplot(3, 3, i+1)# (nrows, ncols, index)
    plt.imshow(img) # muestra la imagen por pantalla
    plt.title(f"Tamaño: {img.shape[:2][0]} x {img.shape[:2][1]} pixeles")#le colocas un titulo a la immagen
    plt.axis("off") #no quiero que me saque ejes porque es una grafica, estoy mostrando simplemente imagenes

#plt.show()# para que muestre toda la composicion

#luego de ver esta parte nos damos cuenta que no todas las fotos tienen las mismas dimensiones por lo que tenemos que normalizar el tamaño

image_size = (180, 180)
batch_size = 128 # tamaño de lote que en deep lerning se utiliza para eficientar el procesamiento de datos y consiste en que se van procesando varias imagenes en paralelo (128)

train_ds = keras.utils.image_dataset_from_directory(
    DATASET_PATH,#donde se encuentra nuestro conjunto de datos
    validation_split=0.2,#dejaremos un 80% para el subconjunto de datos de entrenamiento y el 20% para el subconjunto de datos de validacion 
    subset="training",
    seed=1337, # indicamos una semilla
    image_size=image_size, #tamaño de las imagenes
    batch_size=batch_size, #tamaño del batch_size
)

# chequeamos que todas las imagenes tienen el mismo tamaño

plt.figure(figsize=(10,10))

for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(f"Tamaño: {images[i].shape[0]} x {images[i].shape[1]} pixeles")
        plt.axis("off")
plt.show()      

batch1 = list(train_ds.take(1))
batch1 # te muestra una matriz con la intensidad de los pixeles y una matriz con una etiqueta en cada posicion con 1 si es perro y cero si es gato

print(f"numero de imagenes en el batch: {len(batch1[0][0])}")
print(f"Etiquetas del batch: {batch1[0][1]}")

#mostramos dos imagenes del batch con su etiqueta
plt.figure(figsize=(10, 10))

for img, etiqueta in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i+1)
        plt.imshow(img[i].numpy().astype("uint8"))
        plt.title(f"Etiqueta: {etiqueta[1]}")
        plt.axis("off")
plt.show()

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
#existen otras formas mas especificas de dividir el conjunto de datos si necesitamos aplicar transformaciones concretas. una de las mejores funciones que hay que realizar esta tarea es train_test_split de Sklearn(min 42:40)


#ahora si tenemos nuestro conjunto de datos perfectamente armado para pasarselo a la red neuronal profunda

#queremos que la primera capa tenga 384 neuronas, la segunda 256, la tercera 128 y la ultima capa una neurona el dice que esto es claro ya que tenemos dos opciones como resultado, es gato o perro.

from keras import layers

input_shape= (180, 180, 3) #dimension de las imagenes de entrada, es decir las dimensiones de las imagenes que le vamos a proporcionar

fcnn_model= keras.Sequential() #comenzamos a definir nuestra red neuronal utilizando la appi mas sencilla de keras que es Sequential(se llama asi porque vamos a ir definiendo las capas de nuestra red neuronal de manera secuencial)

#entrada de la red neuronal
fcnn_model.add(layers.Input(shape=input_shape))#esta es la primera capa la cual no va a ser de neuronas sino que aprovechando que keras nos lo permite esta capa es para hacer cierto procesamiento sobre los datos que va a recibir la red

#escalamos las imagenes(seria el procesamiento 1)-> nosotros sabemos que rgb puede variar entre 0 y 255, bueno con esto hacemos que se escale ese valor entre 0 y 1.0 debido a que las redes neuronales funcionan mejor sobre ese valor
fcnn_model.add(layers.Rescaling(1.0/255))

#aplana las imagenes para la primera capa densa-> explica el que como nuestra imagen viene en forma de matriz lo que hacemos con esto es transformarla en un vector debido a que la capa es un vector asi de alguna forma "entra"
fcnn_model.add(layers.Flatten())

# estas capas se caracterizan con algo muy importante y es que tienen parametros del modelo, son variables que se van a ir actualizando durante el proceso de entrenamiento, es como si fuese la memoria de la red neuronal
#Layer 1
fcnn_model.add(layers.Dense(384, activation= 'relu'))

#Layer 2
fcnn_model.add(layers.Dense(256, activation='relu'))

#Layer 3
fcnn_model.add( layers.Dense(128, activation= 'relu'))

#Layer 4
fcnn_model.add(layers.Dense(1, activation='sigmoid')) #softmax si son dos o mas clases(creo que se refier a distintos resultados esperados)

fcnn_model.summary()#-> vemos un resumen de toda la configuracion de la red neuronal

#58:28 explica cosas relacionada con la red mostrandote aspectos de la misma que me lo salte pero se podria retomar

#ahora que ya tenemos la arquitectura de la red neuronal artificial tenemos que configurar la misma

#tenemos que seleccionar tres componentes adicionales para la red neuronal: la funcion de error, la funcion de optimizacion, metricas para monitorizar el proceso de entrenaminto 


#para poder definir los componentes anteriores nosotros utilizamos el metodo compile de keras
fcnn_model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.Adam(1e-3), metrics=['accuracy'])

#entrenamiento de la red neuronal
#para el entrenamiento le damos los datos para actualizar los parametros del modelo que seria en este caso el subconjunto de entrenamiento, un valor(epochs) que dice las vueltas que va a dar sobre todos los ejemplos de nuestro conjunto de datos durante e proceso de entrenamiento(en este caso 10 vueltas) y por ultimo el subconjunto de validacion para que haga pruebas cada vez que recorrra los datos y pueda ir mostrandonos que tal se va comportando nuestra red neuronal  
history = fcnn_model.fit(train_ds, epochs=25, validation_data=val_ds)

# almacenamiento del modelo en el disco -> lo que vamos a almacenar es: la arquitectura del modelo, los parametros del modelo, los hiperparametros del modelo y las metricas

fcnn_model.save("C:\Users\Usuario\Desktop\progra ia(2024)")


