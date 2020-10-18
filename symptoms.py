import pandas as pd
import math


class Symptoms:

    def __init__(self, file):
        self._data = pd.read_csv(file)
        self.symptoms = set()
        for col_name in self._data.columns:
            self.symptoms.add(col_name)
        self.pain_set = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "1", "2", "3",
                         "4", "5", "6", "7", "8", "9", "10"}

    @property
    def data(self):
        return self._data

    def get_possibilities(self, symptom):
        return self._data.loc[:, symptom]

    def find_symptom(self, sentence):
        for word in sentence.split():
            if word in self.symptoms:
                return word
        return None

    def make_diagnosis(self, possibilities, pain):
        index = int(math.floor((pain - 1) / 3))
        return possibilities.iloc[index]

    def find_pain(self, sentence):
        for word in sentence.split():
            if word in self.pain_set:
                return self.convert_string_to_num(word)
        return None

    def convert_string_to_num(self, pain):
        if pain == "one" or pain == "1":
            return 1
        elif pain == "two" or pain == "2":
            return 2
        elif pain == "three" or pain == "3":
            return 3
        elif pain == "four" or pain == "4":
            return 4
        elif pain == "five" or pain == "5":
            return 5
        elif pain == "six" or pain == "6":
            return 6
        elif pain == "seven" or pain == "7":
            return 7
        elif pain == "eight" or pain == "8":
            return 8
        elif pain == "nine" or pain == "9":
            return 9
        elif pain == "ten" or pain == "10":
            return 10
