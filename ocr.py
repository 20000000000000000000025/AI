# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"c:\Program Files\Tesseract-OCR\tesseract.exe"

# a = Image.open('영어문서.jpg')
# result = pytesseract.image_to_string(a, lang = 'eng')
# print(result)

# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

# custom_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# a = Image.open('배격화면1.png')
# result = pytesseract.image_to_string(a, lang='kor')
# print(result)


# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# custom_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

# a = Image.open('배격화면1.png')


# result = pytesseract.image_to_string(a, lang='kor', config=custom_config)

# print(result)


# import pytesseract
# from PIL import Image


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# custom_config = r'--tessdata-dir C:\Program Files\Tesseract-OCR\tessdata'


# a = Image.open('배격화면1.png')

# result = pytesseract.image_to_string(a, lang='kor', config=custom_config)

# print(result)


# import pytesseract
# from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\user\Documents\Tesseract-OCR\tesseract.exe"

# img = Image.open("영어문서_test.png")
# result = pytesseract.image_to_string(img, lang='eng')
# print(result)


# import pytesseract
# from PIL import Image

# # 정확한 Tesseract 실행 경로 지정
# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\user\Documents\Tesseract-OCR\tesseract.exe"

# # 이미지 열기
# img = Image.open("영어단어장.png")

# # OCR 실행 (lang은 'eng' 또는 'kor')
# result = pytesseract.image_to_string(img, lang='kor+eng')


# print(result)



## "C:\Users\user\Desktop\영어 말하기 수행평가 자료\영어단어장.png"
## "C:\users\user\Pictures\Screenshots\영어문서_test.jpg"


import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\user\Documents\Tesseract-OCR\tesseract.exe"

image_path = input("이미지 파일 경로를 입려하시오: ")

try:
    if os.path.exists(image_path):
        img = Image.open(image_path)
        result = pytesseract.image_to_string(img, lang = 'kor+eng')
        print(result)
    else:
        print("파일이 존재하지 않습니다")
        
except Exception as e:
    print("오류 발생", e)
        

