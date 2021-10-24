import os
import platform
from shutil import move
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from pykospacing import Spacing
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

from ocr.models import OcrText

media_root = getattr(settings, "MEDIA_ROOT", 'media')

pytesseract.pytesseract.tesseract_cmd = r'/local/Cellar/tesseract/4.1.1/bin/tesseract'
os_name = platform.system()
if os_name == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

@api_view(['POST'])
def ocr(request):
    info = 'info'
    title = ''
    text = ''
    error_message = ''
    image_path = ''
    if request.FILES:
        file = request.FILES['file']
        print('File Name : {}'.format(file.name))
        if file.name.lower().endswith(('.png', '.jpg', 'jpeg', '.gif')):
            info = 'success'
            title = '텍스트 인식'
            ocr_result = ''
            ocr_text = ''

            fs = FileSystemStorage()
            fname = fs.save(file.name, file)
            upload_fname = os.path.join(media_root, file.name)
            move(os.path.join(media_root, fname), upload_fname)
            image_path = 'media/' + os.path.basename(upload_fname)

            img = Image.open(upload_fname) 
            ocr_result = pytesseract.image_to_string(img, lang='kor+eng') 
            print(f'[OCR TEXT]\n{ocr_result}')

            # ocr_result = ocr_result.strip()
            # ocr_result = ocr_result.replace(' ', '').replace('\n', '')
            # spacing = Spacing()
            # for i, v in enumerate(ocr_result):
            #     ocr_result[i] = spacing(v)
            # ocr_text = "\n".join(ocr_result)

            OcrText.objects.update_or_create(file=file, defaults={'text':ocr_result})

        else:
            error_message = '업로드가 허용되지 않는 파일타입니다.'

    res = {
        'error_message': error_message, 
        'image_path': image_path,
        'ocr_text': ocr_result, 
    }
    return JsonResponse(res)
