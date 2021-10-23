# Vision AI 서비스 

## 1. 파이썬 가상환경 생성 및 실행
- python –m venv venv 
- Windows : venv\Scripts\activate.bat
- MacOS : source venv/bin/activate
- Linux : source venv/bin/activate

## 2. 소스 다운로드
git clone https://github.com/kgpark88/mserver

## 3. 파이썬 패키지 설치
- pip install django
- pip install pandas
- pip install matplotlib
- pip install scipy
- pip install tensorflow
- pip install tensorflow_hub
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

## 4. 테이블 생성
- cd server
- python manage.py migrate
- python manage.py makemigrations ocr
- python manage.py migrate ocr

## 5. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 6. 백엔드 서버 실행
- python manage.py runserver

## 7. 프론트엔드 소스 다운로드 
- https://github.com/kgpark88/mclient

## 8. NPM 패키지 설치 
- npm run install

## 9. 프론트엔드 실행
- npm run serve