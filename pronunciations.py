
'''
Tool that helps in phonetic transcription. Enter a text and it will transcribe it automatically without considering the weak forms.
'''
import requests
import re
import nltk
# Download nltk resources (if not already downloaded)
nltk.download('punkt')

def punctuation_removal(raw_input):
    tokenizer = nltk.RegexpTokenizer(r"\b\w+(?:'\w+)?\b")
    words_without_punctuation = tokenizer.tokenize(raw_input.lower())
    return words_without_punctuation

def main():
    raw_input = input("Please insert the word in English that you want to be transcribed!\n")
    final_phonetic_transcription = '/ '

    # TODO: fix the edgecase 'i'; eventually find a better way to search for 'phonetic' key

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
    main()