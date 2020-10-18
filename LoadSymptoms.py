import pandas as pd


def load_symptoms(symptomFile):
    data = pd.read_csv(symptomFile)
    return data


def get_diagnosis(data, symptom):
    results = data.loc[:, symptom]
    output = ''
    for result in results:
        output += result + " "
    return output

def find_symptoms(data, sentence):
    symptoms = set()
    for col_name in data.columns:
        symptoms.add(col_name)
    print(symptoms)
    for word in sentence.split():
        if word in symptoms:
            print(word + ": found")
        else:
            print(word + ": not found")
