from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
import os
import speech_recognition as sr
import webbrowser as wb
from googletrans import Translator, constants
from pprint import pprint




r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()
globaltext=""
p=False


while(True):

	with sr.Microphone() as source:
		print('Say command to hover over functionalities')
		print('You can give command now:')
		audio = r3.listen(source)



		if 'extract text' in r3.recognize_google(audio):
			r2 = sr.Recognizer()
			path_to_tesseract = r"C:\Users\harsh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
			image_path = r"C:\Users\harsh\Desktop\AU\ImageData\noisy.png"


			with sr.Microphone() as source:
				print('Image Name: ')
				audio = r2.listen(source)


				try:
					get=r2.recognize_google(audio)
					print(image_path[:-9]+get+".png")
					txt = image_path[:-9]+get+".png"

					img = Image.open(txt)

					pytesseract.tesseract_cmd = path_to_tesseract
					text = pytesseract.image_to_string(img)
					globaltext=text

					#print(text[:-1])
					p=True
					print("Extracted data from img file: ")
					print(text[:-1])




				except sr.UnknownValueError:
					print('Error')
				except sr.RequestError as e:
					print('Failed'.format(e))

		if 'text to audio' in r3.recognize_google(audio):
			mytext = globaltext
  

			language = 'en'
  

			myobj = gTTS(text=mytext, lang=language, slow=False)
  

			myobj.save("welcome.mp3")
  

			os.system("welcome.mp3")
				

			
				

				
	if 'translator' in r3.recognize_google(audio):
		translator = Translator()
		print("Enter the text you wish to transltate to English: ")
		lang = input()
		translation = translator.translate(lang)
		print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

	if 'auto' in r3.recognize_google(audio):
		p = Translator()
		# translates the text into french language
		k = p.translate(globaltext, dest='french')
		#converts the result into string format
		translated = str(k.text)

		print(translated)
				
				

	if 'break' in r3.recognize_google(audio):
		break







# path_to_tesseract = r"C:\Users\harsh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
# image_path = r"C:\Users\harsh\Desktop\AU\ImageData\noisy.png"

# img = Image.open(image_path)

# pytesseract.tesseract_cmd = path_to_tesseract
# text = pytesseract.image_to_string(img)

# #print(text[:-1])
# print("Extracted data from img file: ")
# print(text[:-1])

# mytext = text[:-1]
  
# # Language in which you want to convert
# language = 'en'
  
# # Passing the text and language to the engine, 
# # here we have marked slow=False. Which tells 
# # the module that the converted audio should 
# # have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
  
# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("welcome.mp3")
  
# # Playing the converted file
# os.system("welcome.mp3")

