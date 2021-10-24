import os
import sys
import numpy as np
from shutil import move
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.keras import layers

media_root = getattr(settings, "MEDIA_ROOT", 'media')

model_path = "saved_models/flower_classifier"
model = tf.keras.models.load_model(model_path)
class_names = ['Daisy', 'Dandelion', 'Roses', 'Sunflowers', 'Tulips']

@api_view(['POST'])
def classification(request):
    info = 'info'
    title = ''
    text = ''
    error_message = ''
    image_path = ''
    predicted_label = ''
    if request.FILES:
        file = request.FILES['file']
        print('File Name : {}'.format(file.name))
        if file.name.lower().endswith(('.png', '.jpg', '.gif')):
            info = 'success'
            title = '이미지 분류'
            image_url = ''

            fs = FileSystemStorage()
            fname = fs.save(file.name, file)
            upload_fname = os.path.join(media_root, file.name)
            move(os.path.join(media_root, fname), upload_fname)
            image_path = 'media/' + os.path.basename(upload_fname)

            image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224,224))
            input_arr = tf.keras.preprocessing.image.img_to_array(image)
            input_arr = np.array([input_arr/255])  # Convert single image to a batch.
            print(f'[input_arr]\n{input_arr}')

            prediction = model.predict(input_arr)
            predicted_id = np.argmax(prediction, axis=-1)
            predicted_label = class_names[predicted_id[0]]
            print('='*60)
            print(f'prediction : {prediction}')
            print(f'predicted_id : {predicted_id}')
            print(f'predicted_label : {predicted_label}')

        else:
            info = 'info'
            error_message = '업로드가 허용되지 않는 파일타입니다.'

    res = {
        'info': info, 
        'error_message': error_message, 
        'image_path': image_path,
        'predicted_label': predicted_label, 
    }
    return JsonResponse(res)
