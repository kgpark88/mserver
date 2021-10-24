import numpy as np
import matplotlib.pylab as plt
import PIL.Image as Image

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers

feature_extractor_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/2"
file_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
label_url = 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
save_path = '/tmp/flower_photos'
model_export_path = "/tmp/saved_models/flower_classifier"

IMAGE_SHAPE = (224, 224)

data_root = tf.keras.utils.get_file(save_path, file_url, untar=True)
image_generator = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
image_data = image_generator.flow_from_directory(str(data_root), target_size=IMAGE_SHAPE)

labels_path = tf.keras.utils.get_file('ImageNetLabels.txt', label_url)
imagenet_labels = np.array(open(labels_path).read().splitlines())

for image_batch, label_batch in image_data:
    print("Image batch shape: ", image_batch.shape)
    print("Label batch shape: ", label_batch.shape)
    break

feature_extractor_layer = hub.KerasLayer(feature_extractor_url,
                                         input_shape=(224,224,3))

feature_extractor_layer.trainable = False

model = tf.keras.Sequential([
    feature_extractor_layer,
    layers.Dense(image_data.num_classes, activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='categorical_crossentropy',
    metrics=['acc'])

model.fit_generator(image_data, epochs=2)
model.save(model_export_path, save_format='tf')

class_names = sorted(image_data.class_indices.items(), key=lambda pair:pair[1])
print(class_names)
print(class_names)
print(class_names)
class_names = np.array([key.title() for key, value in class_names])
print(class_names)
print(class_names)

model = tf.keras.models.load_model(model_export_path)
predicted_batch = model.predict(image_batch)
predicted_id = np.argmax(predicted_batch, axis=-1)
predicted_label_batch = class_names[predicted_id]
label_id = np.argmax(label_batch, axis=-1)

plt.figure(figsize=(10,9))
plt.subplots_adjust(hspace=0.5)
for n in range(30):
    plt.subplot(6,5,n+1)
    plt.imshow(image_batch[n])
    color = "green" if predicted_id[n] == label_id[n] else "red"
    plt.title(predicted_label_batch[n].title(), color=color)
    plt.axis('off')
    plt.suptitle("Model predictions (green: correct, red: incorrect)")
plt.show()