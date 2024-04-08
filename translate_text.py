import sys
import googletrans
def translate_text(input_text_path, output_translated_text_path, target_language):

    with open(input_text_path, 'r', encoding='utf-8') as file:
                text = file.read()

    translator = googletrans.Translator()

    translation = translator.translate(text, dest=target_language)

    #output text into file
    with open(output_translated_text_path, 'w', encoding='utf-8') as file:
                 file.write(translation.text)

if __name__ == "__main__":

    # Extract command-line arguments
    input_text_path = sys.argv[1]
    output_translated_text_path = sys.argv[2]
    target_language=sys.argv[3]
    
translate_text(input_text_path, output_translated_text_path, target_language)