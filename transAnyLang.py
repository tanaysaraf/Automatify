# adds image processing capabilities
from PIL import Image

# will convert the image to text string
from pytesseract import pytesseract

# translates into preferred language
from googletrans import Translator, constants

# assigning an image from the source path
#img = Image.open('noisy.png')

# converts the image to result and saves it into result variable
#result = pytesseract.image_to_string(img)




path_to_tesseract = r"C:\Users\harsh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\harsh\Desktop\AU\ImageData\noisy.png"

img = Image.open(image_path)

pytesseract.tesseract_cmd = path_to_tesseract
result = pytesseract.image_to_string(img)

p = Translator()
# translates the text into french language
k = p.translate(result, dest='french')
#converts the result into string format
translated = str(k.text)

print(translated)

# with open('test.txt', mode ='w') as file:
#   file.write(result)
#   file.write("\n")
#   file.write(translated)
#   print("ready!")