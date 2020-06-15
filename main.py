import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

#Recording the voice
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

# 
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

# Recording the voice 
def steve_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# Responding to the voice
def respond(voice_data):
    # Name
    if 'what is your name' in voice_data:
        steve_speak('My name is Steve')

    # Time
    if 'what time is it' in voice_data:
        steve_speak(ctime())

    # Google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        steve_speak(f'Here is what I found for {search_term} on google')

    # Location
    if there_exists(["where is"]):
        search_term = voice_data.split("is")[-1]
        url = f"https://google.nl/maps/place/{search_term}"
        webbrowser.get().open(url)
        steve_speak(f'Here is the location of {search_term}')
    # Leave
    if 'exit' in voice_data:
        steve_speak('Goodbye')
        exit()

# Running the program
wake_word = "hey steve"

while True:
    print("Listening...")
    voice_data = record_audio()

    if wake_word in voice_data:
        steve_speak('How can I help you?')
        voice_data = record_audio()
        respond(voice_data)

