from google.cloud import texttospeech
import os
import tika
from tika import parser
from tkinter import *
from tkinter import filedialog

# tika server
tika.initVM()

# creating window
window = Tk()
window.title('PDF to Audiobook')
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

# defining functions
def get_path():

    path = filedialog.askopenfilename(title='Open PDF', filetypes=(('pdf files', '*.pdf'),))
    get_text(path)


def get_text(path):
    parsed = parser.from_file(path)
    text = parsed['content']
    convert(text)

def convert(text):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'YOUR CREDENTIALS'

    client = texttospeech.TextToSpeechClient()
    input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)

    os.startfile('output.mp3')


# button to get path
button = Button(width=10, height=5, command=get_path, text="Select PDF\n and\n Convert it")
button.pack()

window.mainloop()
