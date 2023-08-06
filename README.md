This basic tool uses the dictionary api (https://dictionaryapi.dev/) to phonetically transcribe inserted text/file in the CLI.

1. Installation

pip install -r requirements.txt

2. Usage
Simply run the script with:
python3 pronunciations.py
Otherwise use the -i flag to input a text file
python3 pronunciations.py -i ~/my_textfile.txt

2. To do:
- Improve script lookup efficiency with the json module
- Change the script logic to store the already known transcriptions

3. Done
- Support inserting files with text in order to produce entire output files for IPA 
- X-SAMPA support (get info from the api and def a function to convert the characters from a dictionary)
   
4. Challanges:
- Weak form support
- Connected speech support
- Homophone support