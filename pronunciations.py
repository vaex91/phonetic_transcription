
'''
Tool that helps in phonetic transcription. Enter a text and it will transcribe it automatically without considering the weak forms.
'''
import requests
import re
import nltk
import argparse
from pathlib import Path

# Download nltk resources (if not already downloaded)
nltk.download('punkt')
parser = argparse.ArgumentParser()
# TODO: implement -i as user input for text files and -o as user output (as a .txt file)
# TODO: implement a loading bar that would take a total number of words and show the speed and eta

def file_reader(text_file) -> str:
    read_file = open(text_file, 'r')
    return read_file.readline()

def punctuation_removal(raw_input) -> str:
    tokenizer = nltk.RegexpTokenizer(r"\b\w+(?:'\w+)?\b")
    words_without_punctuation = tokenizer.tokenize(raw_input.lower())
    return words_without_punctuation

def main():
    raw_input = input("Please insert the word in English that you want to be transcribed!\n")
    final_phonetic_transcription = '/ '
    # import the file
    text_file = Path('~/test.txt').expanduser()
    # prepare the file for transcription
    raw_file = file_reader(text_file)
    clean_text = punctuation_removal(raw_file)
    # print the clean text
    print(clean_text)

    # TODO: fix the edgecase 'i'; eventually find a better way to search for 'phonetic' key
    # TODO: apply json for better script management

    for word in punctuation_removal(raw_input):
        get_data = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
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

if __name__ == "__main__":
#    parser.add_argument("-input", "-i", required=False, help="typle in the path to the file that you want to transcribe")
    main()