import datetime

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(audio):
    print('\nUltron : '+audio)
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak('Good Morning')
    elif (hour >= 12) and (hour < 18):
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('Hello I am Ultron. How may I help you')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)  # here
        print('Listening...')
        # r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en-IN')
        speak(query)
    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    return query


if __name__ == '__main__':

    wish_me()

    while True:
        take_command()
        if 'q' == input('\nEnter "Q" to Exit or press any other key : ').lower():
            break
