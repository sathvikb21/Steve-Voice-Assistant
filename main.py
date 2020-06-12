import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            steve_speak('Sorry, I did not get that')
        except sr.RequestError:
            steve_speak('Can not connect to the internet')
        return voice_data.lower()


def steve_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        steve_speak('My name is Steve')
    if 'what time is it' in voice_data:
        steve_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        steve_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        steve_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        steve_speak('Goodbye')
        exit()

wake_word = "hey steve"

while True:
    print("Listening...")
    voice_data = record_audio()

    if voice_data.count(wake_word) > 0:
        steve_speak('How can I help you?')
        voice_data = record_audio()
        respond(voice_data)

