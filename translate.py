import deepl

def translate_file(input_filepath, output_filepath):
    translator = deepl.Translator() #initialize the translator with public API key
    
    with open(input_filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(output_filepath, 'w', encoding='utf-8') as file:
        for line in lines:
            #strip newline chars and any whitespace
            original_text = line.strip()
            
            #translate
            result = translator.translate_text(original_text, source_lang="ES", target_lang="EN-US")
            
            #write to the output file
            file.write(f"{original_text};{result.text}\n")
            
#define the input/output file paths
input_filepath = 'spanish-vocabulary.txt'
output_filepath = 'spanish-vocab-final.txt'

translate_file(input_filepath, output_filepath)