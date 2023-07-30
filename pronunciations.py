
'''
Tool that helps in fonetic transcription. Enter a text and it will transcribe it automatically without considering the weak forms.
'''
import requests
import re
import nltk
# Download nltk resources (if not already downloaded)
nltk.download('punkt')

raw_input = input("Please insert the word in English that you want to be transcribed!\n")

def punctuation_removal(raw_input):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    words_without_punctuation = tokenizer.tokenize(raw_input.lower())
    return words_without_punctuation


# testing fetching the data
get_data = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{raw_input}')

# TODO: create a function for that and then use it in a loop

if get_data.status_code == 200:
    store_data = get_data.json()
    phonetics_string = store_data[0]['phonetics']
    phonetic_transcription = phonetics_string[1]['text']
elif get_data.status_code == 404:
    print('Sorry, word not found.')   
else: 
    print(f'API request failed with status code {get_data.status_code}')

print(phonetic_transcription)