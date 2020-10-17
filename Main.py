from playsound import playsound
import TexttoSpeech

f = open("lorem ipsum.txt")

playsound(TexttoSpeech.convert_to_speech(f.read()))

f.close()
