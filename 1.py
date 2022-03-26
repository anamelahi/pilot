import speech_recognition as sr                   #importing modules
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
	
	pilot = pyttsx3.init()
	pilot.say(command)
	pilot.runAndWait()
	
	

while(1):
	
	try:
		
		with sr.Microphone() as source2:
			
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			audio2 = r.listen(source2)
			
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print(MyText)                                    #prints what we speak
			SpeakText(MyText)                                #speaks what's printed
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("Please say again")

