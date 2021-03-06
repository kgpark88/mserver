# Vision AI 서비스 서버 

## 1. 파이썬 가상환경 생성 및 실행
### Windows
- python –m venv venv 
- venv\Scripts\activate.bat
### MacOS/Linux
- python3 -m venv venv
- source venv/bin/activate

## 2. TesseractOCR 설치
### Windows
- 설치파일 다운로드 : https://github.com/UB-Mannheim/tesseract/wiki
- 참조 : https://turtle-dennis.tistory.com/29  
### macOS
- brew install tesseract
- brew install tesseract-lang
- 참조 : https://tariat.tistory.com/703  
### Linux
- apt-get install tesseract-ocr
- 참조 : https://linuxhint.com/install-tesseract-ocr-linux/

### kor.traineddata 파일 다운로드 
- 다운로드 : https://github.com/tesseract-ocr/tessdata/ 에서 kor.traineddata 다운로드
- https://github.com/tesseract-ocr/tessdata/blob/main/kor.traineddata
- Windows : C:\Program Files\Tesseract-OCR\tessdata\ 디렉토리에 복사
- MacOS/Linux : /usr/local/Cellar/tesseract/4.1.1/share/tessdata/ 디렉토리에 복사 
- cp Downloads/kor.traineddata /usr/local/Cellar/tesseract/4.1.1/share/tessdata/.

## 3. 서버프로그램 소스 다운로드
- git clone https://github.com/kgpark88/mserver

## 4. 파이썬 패키지 설치
- pip install pandas
- pip install matplotlib
- pip install scipy
- pip install django
- pip install django-import-export
- pip install django-cors-headers
- pip install djangorestframework
- pip install django-rest-swagger
- pip install drf-yasg
- pip install django-crispy-forms
- pip install opencv-python
- pip install Pillow
- pip install pytesseract
- pip install git+https://github.com/haven-jeon/PyKoSpacing.git
- pip install git+https://github.com/ssut/py-hanspell.git
- pip install tensorflow
- pip install tensorflow_hub

## 5. 테이블 생성
- cd mserver
- python manage.py makemigrations ocr
- python manage.py migrate 

## 6. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 7. 백엔드 서버 실행
- python manage.py runserver

## 8. 백엔드 웹서비스 접속
- http://localhost:8000

## 실행화면
![image](https://user-images.githubusercontent.com/17672596/142606611-9a9249d1-816f-45c2-98ef-f99826d3b2ad.png)

![image](https://user-images.githubusercontent.com/17672596/142606630-c1f561ed-2de1-4ce9-bc2b-90472e786459.png)

![image](https://user-images.githubusercontent.com/17672596/142606643-1def09c4-03d6-46b0-a921-9e7a4ba38b7d.png)




