import datetime
import random

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)


def speak(audio, speaker='Ultron'):
    print(f'\n{speaker} : {audio}')
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
        response = r.recognize_google(audio)
        speak(response, speaker='User')
    except Exception as e:
        print(e)
        speak('Say that again please...')
        response = take_command()
        return response
    return response.lower()


def teacher():
    alphabet = random.choice('abcdefghijklmnopqrstuvwxyz')
    alphabet_objects = {
        'a': ['alligator', 'ambulance', 'anchor', 'ant', 'anteater', 'apple', 'aquarium', 'astronaut'],
        'b': ['balloon', 'baker', 'bat', 'bear', 'bee', 'boat', 'broccoli', 'butterfly'],
        'c': ['candle', 'car', 'cat', 'clown', 'cow', 'caterpillar', 'crab', 'crocodile'],
        'd': ['daisy', 'deer', 'dinosaur', 'dog', 'dolphin', 'donkey', 'dove', 'duck'],
        'e': ['egg', 'elephant', 'elk', 'envelope', 'eagle', 'earwig', 'easel', 'eel'],
        'f': ['farmer', 'fire', 'fish', 'five', 'flag', 'flower', 'frog', 'fruit'],
        'g': ['garden', 'gift', 'goat', 'goose', 'gorilla', 'grapes', 'grasshopper', 'groundhog'],
        'h': ['hare', 'heart', 'hen', 'hippo', 'horse', 'house'],
        'i': ['igloo', 'iguana', 'ink', 'insect'],
        'j': ['jar', 'jeep', 'jellyfish', 'jester', 'jet'],
        'k': ['king', 'kite', 'kitten', 'koala'],
        'l': ['ladybug', 'lamb', 'leaf', 'lily', 'lion', 'lobster'],
        'm': ['monkey', 'moon', 'moose', 'mouse'],
        'n': ['nest', 'nine', 'numbers', 'nurse'],
        'o': ['octopus', 'ostrich', 'otter', 'ox', 'oak', 'ocean', 'oval', 'overalls'],
        'p': ['panda', 'penguin', 'pig', 'pumpkin'],
        'q': ['quail', 'queen', 'quetzal', 'quilt'],
        'r': ['rabbit', 'raccoon', 'rainbow', 'rat', 'reindeer', 'rooster'],
        's': ['sand dollar', 'snail', 'snake', 'snowman', 'spider', 'starfish'],
        't': ['tiger', 'toad', 'tractor', 'tree', 'turkey', 'turtle'],
        'u': ['unicorn', 'universe', 'unicycle', 'utensil'],
        'v': ['van', 'violin', 'volcano', 'vulture'],
        'w': ['walrus', 'watermelon', 'wolf', 'woodpecker'],
        'x': ['X-ray', 'xylophone', 'ox', 'fox'],
        'y': ['yacht', 'yak', 'yarn', 'yoyo'],
        'z': ['zebra', 'zigzag', 'zipper', 'zoo'],
    }
    alphabet_objects = random.choice(alphabet_objects[alphabet])
    sentence = f'{alphabet} for {alphabet_objects}'
    speak(sentence)
    return sentence.lower()


if __name__ == '__main__':
    wish_me()

    while True:
        sentence = teacher()
        response = take_command()
        if sentence == response:
            speak('You are Correct')
        else:
            speak('You are not Correct')
            speak(f'Correct Sentence is {sentence}')
        if 'q' == input('\nEnter "Q" to Exit or press any other key : ').lower():
            break

