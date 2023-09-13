# Importing necessary modules required
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import pyttsx3

flag = 0

# A tuple containing all the language and
# codes of the language will be detcted
dic = ('english', 'en', 'hindi', 'hi', 'tamil', 'ta',)


# Capture Voice
# takes command through microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='ta-in')
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query
def takecommand1():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query


# Input from user
# Make input to lowercase
query = takecommand()
while (query == "None"):
    query = takecommand()


def destination_language():
    print("Enter the language in which you\
    want to convert : Ex. Hindi , English , etc.")
    print()

    # Input destination language in
    # which the user wants to translate
    to_lang = takecommand1()
    while (to_lang == "None"):
        to_lang = takecommand1()
    to_lang = to_lang.lower()
    return to_lang


to_lang = destination_language()

# Mapping it with the code
while (to_lang not in dic):
    print("Language in which you are trying\
    to convert is currently not available ,\
    please input some other language")
    print()
    to_lang = destination_language()

to_lang = dic[dic.index(to_lang) + 1]

# invoking Translator
translator = Translator()

# Translating from src to dest
text_to_translate = translator.translate(query, dest='en-in')

text = text_to_translate.text

# Using Google-Text-to-Speech ie, gTTS() method
# to speak the translated text into the
# destination language which is stored in to_lang.
# Also, we have given 3rd argument as False because
# by default it speaks very slowly
speak = gTTS(text=text, lang=to_lang, slow=False)

# Using save() method to save the translated
# speech in capture_voice.mp3
speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
os.remove('captured_voice.mp3')

# Printing Output
print(text)
