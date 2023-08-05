
'''
Tool that helps in phonetic transcription. Enter a text and it will transcribe it automatically without considering the weak forms.
'''
import requests
import re
import nltk
import argparse
from pathlib import Path

# TODO: implement -i as user input for text files and -o as user output (as a .txt file)
# TODO: implement a loading bar that would take a total number of words and show the speed and eta
# TODO: eventually more object-oriented to speed up the script; store the already fetched data 

def arg_parse():
    parser = argparse.ArgumentParser(
        prog='phonetic_transcriber.py',
        description='Tool that helps in phonetic transcription. Enter a text or a file as input (-i) and it will transcribe it automatically without considering the weak forms.')
    parser.add_argument("-input", "-i", type=Path, required=False, help="Type in the path to the file that you want to transcribe; i.e.: -i ~/my_text.txt")
    args = parser.parse_args()
    
    if args.input:
        print(f'File path provided: {args.input}, processing...')
        return args
    else:
        print('No file path provided. Proceeding with typed text.')

def file_reader(text_file) -> str:
    with open(text_file, 'r') as read_file:
        content = read_file.read()
        return content

def punctuation_removal(input) -> list:
    tokenizer = nltk.RegexpTokenizer(r"\b\w+(?:'\w+)?\b")
    words_without_punctuation = tokenizer.tokenize(input.lower())
    return words_without_punctuation

def transcribe():
    args = arg_parse()
    # Check if file has been inserted
    if args == None:
        raw_input = input("Please insert the word in English that you want to be transcribed!\n")
    else:
        text_file = args.input.expanduser()
        raw_input = file_reader(text_file)

    final_phonetic_transcription = '/ '
     
    # TODO: fix the edgecase 'i'; eventually find a better way to search for 'phonetic' key
    # TODO: apply json for better script management

    for word in punctuation_removal(raw_input):
        get_data = requests.get(f'{dictionary_url}{word}')
        if get_data.status_code == 200:
            store_data = get_data.json()
            # different methods to find the phonetic transcription in the generated .json
            try:
                phonetics_string = store_data[0]['phonetics']
                phonetic_transcription = phonetics_string[1]['text']
            except IndexError:
                phonetic_transcription = store_data[0]['phonetic']
            finally:
                escape_char = re.escape('/') 
                final_phonetic_transcription = final_phonetic_transcription + re.sub(escape_char, '', phonetic_transcription) + ' '
        elif get_data.status_code == 404:
            print(f'Sorry, word "{word}" not found.')   
        else: 
            print(f'API request failed with status code {get_data.status_code}')

    final_phonetic_transcription += '/'
    print(final_phonetic_transcription)

# add X-SAMPA dictionary for its later conversion
    x_sampa = {
        "ɪ": "I",
        "æ": "{",
        "ʌ": "V",
        "ə": "@",
        "ɜ": "E",
        "ɑ": "A",
        "ɒ": "Q",
        "ɔ": "O",
        "ʊ": "U",
        "θ": "T",
        "ð": "D",
        "ʃ": "S",
        "ʒ": "Z",
        "ŋ": "N"
    }

    final_phonetic_transcription_x_sampa = ''
    for character in final_phonetic_transcription:
        if character in x_sampa:
            character = x_sampa[character]
            final_phonetic_transcription_x_sampa += character
        else:
            final_phonetic_transcription_x_sampa += character 
    print(final_phonetic_transcription_x_sampa)

if __name__ == '__main__':
# Download nltk resources (if not already downloaded)
    nltk.download('punkt')
    dictionary_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'
    transcribe()