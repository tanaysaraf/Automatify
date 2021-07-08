
#Python 2.x program for Speech Recognition
  
import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r3=sr.Recognizer()
r2=sr.Recognizer()

with sr.Microphone() as source:
	print('Say command to hover over functionalities')
	print('You can give command now:')
	audio = r3.listen(source)

	if 'video' in r2.recognize_google(audio):
		r2 = sr.Recognizer()
		url = 'https://www.youtube.com/results?search_query='


		with sr.Microphone() as source:
			print('Search Video Name: ')
			audio = r2.listen(source)


			try:
				get=r2.recognize_google(audio)
				print(get)
				wb.get().open_new(url+get)
			except sr.UnknownValueError:
				print('Error')
			except sr.RequestError as e:
				print('Failed'.format(e))


	if 'web search' in r2.recognize_google(audio):
		r2 = sr.Recognizer()
		url = 'https://www.google.com/search?q='


		with sr.Microphone() as source:
			print('Search Web Name: ')
			audio = r2.listen(source)


			try:
				get=r2.recognize_google(audio)
				print("You searched for: ",get)
				wb.get().open_new(url+get)
			except sr.UnknownValueError:
				print('Error')
			except sr.RequestError as e:
				print('Failed'.format(e))

	if 'make text' in r2.recognize_google(audio):
		r2 = sr.Recognizer()
		


		with sr.Microphone() as source:
			print('Speak Now!')
			audio = r2.listen(source)


			try:
				get=r2.recognize_google(audio)
				print(get)
				
			except sr.UnknownValueError:
				print('Error')
			except sr.RequestError as e:
				print('Failed'.format(e))