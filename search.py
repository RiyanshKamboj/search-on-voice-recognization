import speech_recognition as sr
import webbrowser as wb
r2=sr.Recognizer()
r3=sr.Recognizer()
value=0
while(value==0):
   with sr.Microphone() as source:
      print("speak now :search")
      audio= r3.listen(source)
   if 'search' in r2.recognize_google(audio): 
     r2 = sr.Recognizer()
     url ='https://www.google.com/search?q='
     with sr.Microphone() as source:
        print("search query")
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
            value=1
        except sr.UnknownValueError:
            print('error')
        except sr.RequstError as e:
            print('failed'.format(e))
   else:
      print('again')

    
