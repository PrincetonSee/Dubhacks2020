# THIS FILE IS FOR DEMO PURPOSES ONLY

from playsound import playsound
import TexttoSpeech as ts
import SpeechToText as st
from symptoms import Symptoms
import RecordAudio
import time


# Set up symptoms object
symptoms = Symptoms("symptoms.csv")

# Opening Question
playsound(ts.convert_to_speech("How can I help you?"))
print("recording...")
# D: My throat hurts
userInput = RecordAudio.get_recording(2)
result = st.speech_to_text(userInput)
print(result)

# Inquire about symptoms
playsound(ts.convert_to_speech("What are your symptoms?"))
print("recording...")
# # D: I'm hot and my throat feels scratchy
userInput = RecordAudio.get_recording(2.5)
result = st.speech_to_text(userInput)
print(result)
symptom_found = symptoms.find_symptom(result)

# Ask about symptoms again if symptom not found
while symptom_found is None:
    playsound(ts.convert_to_speech("What are your symptoms?"))
    userInput = RecordAudio.get_recording(5)
    result = st.speech_to_text(userInput)
    print(result)
    symptom_found = symptoms.find_symptom(result)

# Look up and save possible diagnosis possibilities
possibilities = symptoms.get_possibilities(symptom_found)

# Ask about pain level
playsound(ts.convert_to_speech("How bad is the pain from 1 to 10?"))
print("recording...")
# # D: Feels like a 6
userInput = RecordAudio.get_recording(2.5)
result = st.speech_to_text(userInput)
print(result)
# pain_calculated = symptoms.find_pain(result)

# Ask about pain level again if not between 1 - 10
# while pain_calculated is None:
#     playsound(ts.convert_to_speech("Rate the pain you feel on a scale of 1 to 10"))
#     userInput = RecordAudio.get_recording(2.5)
#     result = st.speech_to_text(userInput)
#     print(result)
#     pain_calculated = symptoms.convert_string_to_num(result)

# Calculate and save final diagnosis
# diagnosis = symptoms.make_diagnosis(possibilities, pain_calculated)

# Output final diagnosis
playsound(ts.convert_to_speech("Our analysis shows that you may have " + "strep throat"))

playsound(ts.convert_to_speech("Would you like to hold for a doctor to give you a prescription or visit a local free clinic?"))
print("recording...")
# # D: Visit a free clinic
userInput = RecordAudio.get_recording(2.5)
result = st.speech_to_text(userInput)
print(result)

playsound(ts.convert_to_speech("The nearest clinic is Rotacare free clinic, would you like to see the route or view other options?"))
print("recording...")
# # D: See route
userInput = RecordAudio.get_recording(2)
result = st.speech_to_text(userInput)
print(result)

playsound(ts.convert_to_speech("If you would like to send the report to the doctor click the left button, otherwise you may continue and print the directions"))
