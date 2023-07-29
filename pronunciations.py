
'''
Tool that helps in fonetic transcription. Enter a text and it will transcribe it automatically without considering the weak forms.
'''
import requests
import nltk
# Download nltk resources (if not already downloaded)
nltk.download('punkt')

raw_input = input("Please insert the text in English that you want to be transcribed!\n")

def punctuation_removal(raw_input):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    words_without_punctuation = tokenizer.tokenize(raw_input.lower())
    return words_without_punctuation

# TODO

