try:
    from PIL import Image
except ImportError:
    import Image
from PIL import ImageEnhance
import pytesseract
import os


lengthfilesindoc4folder =  len(os.listdir('./JLASH_CATÁLOGO 2023 (7)_compressed'))

for i in range(0, lengthfilesindoc4folder):
    print(f'======================{i}========================= start')

    image = Image.open(f'./JLASH_CATÁLOGO 2023 (7)_compressed/page{i}.jpg')

    ocr_result = pytesseract.image_to_string(image, lang='eng')
    print(ocr_result)
  
    


    # print(indexByApple)

    print(f'======================{i}========================= end')




