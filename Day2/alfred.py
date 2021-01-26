import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):

    engine.say(text)
    #engine.say('What can I do for you')
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please say that again ,Sir')

while True:
    run_alexa()
