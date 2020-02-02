import speech_recognition as sr
import pyaudio

def speech_to_text():
    r1 = sr.Recognizer()
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()

    with sr.Microphone() as source:
        print("Search for Book")
        print("Speak now")
        audio = r3.listen(source)

    print(r2.recognize_google(audio))
    transcript = r2.recognize_google(audio)
    return transcript
