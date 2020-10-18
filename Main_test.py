import sounddevice as sd
import soundfile as sf
import TexttoSpeech as ts
# import SpeechToText as st
import RecordAudio
import os

filename = ts.convert_to_speech("Welcome back Bob, what can I do to help?")
data, fs = sf.read(filename, dtype='float32')
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing
# playsound(ts.convert_to_speech("Welcome back Bob, what can I do to help?"))
#
# userInput = RecordAudio.get_recording(5)
# print(st.speech_to_text(userInput))
#
# playsound(ts.convert_to_speech("What're your symptoms?"))
#
# userInput = RecordAudio.get_recording(5)
# print(st.speech_to_text(userInput))
#
# playsound(ts.convert_to_speech("Rate the pain you feel on a scale of 1 to 10"))
#
# userInput = RecordAudio.get_recording(5)
# print(st.speech_to_text(userInput))
#
# playsound(ts.convert_to_speech("Do you feel any lumps on your throat?"))
#
# userInput = RecordAudio.get_recording(5)
# print(st.speech_to_text(userInput))
#
# playsound(ts.convert_to_speech("Our analysis shows that you may have Strep Throat. Would you like to hold for a doctor "
#                                "to give you a prescription or visit a local free clinic?"))
#
# userInput = RecordAudio.get_recording(5)
# print(st.speech_to_text(userInput))
#
# filename = 'myfile.wav'
# # Extract data and sampling rate from file
# data, fs = sf.read(filename, dtype='float32')
# sd.play(data, fs)
# status = sd.wait()  # Wait until file is done playing