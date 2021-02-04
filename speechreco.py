import speech_recognition as sr

# l = sr.Microphone.list_microphone_names()

# for i in l :
#     print(str(l.index(i))+' '+i)

def startSpeech(value):
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print('say something') #use label to tell the user to start speaking.
        audio = r.record(source,duration=value)
        try:
            print('you said : '+r.recognize_google(audio))
        except Exception as e:
            print('error'+str(e))

startSpeech(30)
