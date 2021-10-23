# Vision AI 서비스 서버 

## 1. 파이썬 가상환경 생성 및 실행
- python –m venv venv 
- Windows : venv\Scripts\activate.bat
- MacOS : source venv/bin/activate
- Linux : source venv/bin/activate

## 2. TesseractOCR 설치
■ Windows
- 설치파일 다운로드 : https://github.com/UB-Mannheim/tesseract/wiki
- 참조 : https://turtle-dennis.tistory.com/29
■ macOS
- brew install tesseract
- brew install tesseract-lang
- 참조 : https://tariat.tistory.com/703
■ Linux
- apt-get install tesseract-ocr
- 참조 : https://linuxhint.com/install-tesseract-ocr-linux/

## 3. 서버프로그램 소스 다운로드
- git clone https://github.com/kgpark88/mserver

## 4. 파이썬 패키지 설치
- pip install django
- pip install pandas
- pip install matplotlib
- pip install scipy
- pip install django-import-export
- pip install django-cors-headers
- pip install djangorestframework
- pip install django-rest-swagger
- pip install drf-yasg
- pip install django-crispy-forms
- pip install opencv-python
- pip install Pillow
- pip install pytesseract
- pip install kss
- pip install git+https://github.com/haven-jeon/PyKoSpacing.git
- pip install git+https://github.com/ssut/py-hanspell.git
- pip install regex
- pip install tensorflow
- pip install tensorflow_hub

## 5. 테이블 생성
- cd mserver
- python manage.py migrate
- python manage.py makemigrations ocr
- python manage.py migrate ocr

## 6. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 7. 백엔드 서버 실행
- python manage.py runserver

## 8. 백엔드 웹서비스 접속
- http://localhost:8000
