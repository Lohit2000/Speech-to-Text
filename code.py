pip install SpeechRecognition
pip install pyaudio

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic:
    print("Say Anything!!!!!!!!")
    audio = r.listen(mic)
print(r.recognize_google(audio))
