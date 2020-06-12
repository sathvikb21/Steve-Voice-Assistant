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


time.sleep(1)
steve_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
