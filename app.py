import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('/home/abhinab/Downloads/female.wav') as source:
    audio = r.record(source)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
