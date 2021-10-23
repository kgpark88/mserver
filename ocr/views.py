import os
import sys
import numpy as np
import cv2   
import pandas as pd
from shutil import move
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from kss import split_sentences
from pykospacing import Spacing
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
media_root = getattr(settings, "MEDIA_ROOT", 'media')

@api_view(['POST'])
def ocr(request):
    info = 'info'
    title = ''
    text = ''
    error_message = ''
    if request.FILES:
        file = request.FILES['file']
        print('AD Check : {}'.format(file.name))
        if file.name.lower().endswith(('.png', '.jpg', '.gif')):
            info = 'success'
            title = '파일을 등록 하였습니다.'
            image_url = ''
            ocr_result = ''
            ocr_text = ''

            fs = FileSystemStorage()
            fname = fs.save(file.name, file)
            upload_fname = os.path.join(media_root, file.name)
            move(os.path.join(media_root, fname), upload_fname)
            image_url = '/media/' + os.path.basename(upload_fname)

            img = Image.open(upload_fname) 
            ocr_result = pytesseract.image_to_string(img, lang='kor+eng') 
            print(f'[OCR Result]\n{ocr_result}')
            ocr_result = ocr_result.strip()
            ocr_result = ocr_result.replace(' ', '').replace('\n', '')
            ocr_result = split_sentences(ocr_result)
            spacing = Spacing()
            for i, v in enumerate(ocr_result):
                ocr_result[i] = spacing(v)
            ocr_text = "\n".join(ocr_result)
        else:
            error_message = '업로드가 허용되지 않는 파일타입니다.'
    res = {
        'error_message': error_message, 
        'image_url': image_url,
        'ocr_text': ocr_text, 
    }
    print(res)
    return JsonResponse(res)
