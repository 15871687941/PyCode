# from __future__ import division 精度计算
from PIL import Image
import pytesseract

image = Image.open("cap01.jpg")
result = pytesseract.image_to_string(image)
print(result)