import soundfile as sf
import speech_recognition as sr


def recognize(filename):

    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language="pt-BR")

        print(text)


for i in range(1, 8):
    try:
        filename = f'my_record/{i}.wav'
        # recognize(filename)
        ob = sf.SoundFile(filename)
        print('Sample rate: {}'.format(ob.samplerate))
        print('Channels: {}'.format(ob.channels))
        print('Subtype: {}'.format(ob.subtype))
    except:
        print(f'~~~~~~ Audio {i}~~~~ñão~~~~')
