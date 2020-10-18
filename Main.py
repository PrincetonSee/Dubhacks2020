from playsound import playsound
import TexttoSpeech as ts
import SpeechToText as st
from symptoms import Symptoms
import RecordAudio
import time
import os


start = time.perf_counter()
# Set up symptoms object
symptoms = Symptoms("symptoms.csv")

# Opening Question
playsound(ts.convert_to_speech("Welcome back Bob, what can I do to help?"))
userInput = RecordAudio.get_recording(2)
result = st.speech_to_text(userInput)
print(result)

# Inquire about symptoms
playsound(ts.convert_to_speech("What are your symptoms?"))
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
playsound(ts.convert_to_speech("Rate the pain you feel on a scale of 1 to 10"))
userInput = RecordAudio.get_recording(2.5)
result = st.speech_to_text(userInput)
print(result)
pain_calculated = symptoms.find_pain(result)

# Ask about pain level again if not between 1 - 10
while pain_calculated is None:
    playsound(ts.convert_to_speech("Rate the pain you feel on a scale of 1 to 10"))
    userInput = RecordAudio.get_recording(2.5)
    result = st.speech_to_text(userInput)
    print(result)
    pain_calculated = symptoms.convert_string_to_num(result)

# Calculate and save final diagnosis
diagnosis = symptoms.make_diagnosis(possibilities, pain_calculated)

# Output final diagnosis
playsound(ts.convert_to_speech("Our analysis shows that you may have " + diagnosis))

end = time.perf_counter()
print(end - start)