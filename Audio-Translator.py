#Python based language Translator
#install these libraries 
import translate
import speech_recognition as sr

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Initialize microphone
microphone = sr.Microphone()

# Record audio from microphone
with microphone as source:
    print("Speak now")
    audio = recognizer.listen(source)

# Perform speech recognition
try:
    text = recognizer.recognize_google(audio, language="hi-IN")
    print("Recognized Text (Hindi):", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand audio.")
    text = ""

# Translate the recognized text to English
if text:
    translator = translate.Translator(from_lang="hi", to_lang="en")
    translated_text = translator.translate(text)
    print("Translated Text (English):", translated_text)

    # Print the translated text in English
    print("Translated Text (English):", translated_text)
else:
    print("No text recognized. Cannot translate.")
