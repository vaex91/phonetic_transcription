This basic tool uses the dictionary api (https://api.dictionaryapi.dev/api/v2/) to phonetically transcribe inserted text in the CLI.

1. Installation

pip install -r requirements.txt

2. Usage
Simply run the script with:
python3 pronunciations "Text I want to to be transcribed" and it will print the output

2. To do:
- Support inserting files with text in order to produce entire output files for IPA 
- X-SAMPA support (get info from the api and def a function to convert the characters from a dictionary)

3. Challanges:
- Weak form support
- Connected speech support
- Homophone support