import subprocess
import sys
def extract_audio(video_path, output_audio_path):
    # Execute script to extract audio
    subprocess.run(['python', 'C:/Users/skfog/OneDrive/Desktop/project/backend/extract_audio.py', video_path, output_audio_path])
   

def audio_to_text(audio_path, output_text_path):
    # Execute script to convert audio to text
    subprocess.run(['python', 'C:/Users/skfog/OneDrive/Desktop/project/backend/audio_to_text.py', audio_path, output_text_path])
   

def translate_text(input_text_path, output_translated_text_path, target_language):
    # Execute script to translate text to another language
    subprocess.run(['python', 'C:/Users/skfog/OneDrive/Desktop/project/backend/translate_text.py', input_text_path, output_translated_text_path, target_language])
   

def text_to_speech(input_text_path, output_audio_path, language_code):
    # Execute script to convert text to speech
    subprocess.run(['python', 'C:/Users/skfog/OneDrive/Desktop/project/backend/text_to_speech.py', input_text_path, output_audio_path, language_code])
    

def merge_audio_to_video(input_video_path, translated_audio_path, output_video_path):
    # Execute script to merge audio to video
    subprocess.run(['python', 'C:/Users/skfog/OneDrive/Desktop/project/backend/lastout.py', input_video_path, translated_audio_path, output_video_path])
    

if __name__ == "__main__":
    # Define paths for intermediate and final files
    # Check if the correct number of arguments are provided
    # if len(sys.argv) != 2:
    #      print("Usage: python extract_audio.py <video_path> <output_audio_path>")
    #      sys.exit(1)

    # # Extract command-line arguments
    
    video_path = sys.argv[1]
    lang = sys.argv[2]
    # video_path="C:/Users/skfog/OneDrive/Desktop/project/demo.mp4"
    # audio_path="C:/Users/skfog/OneDrive/Desktop/project/site/output/output.mp3"
    text_path = "output_text.txt"
    translated_text_path = "output_translated_text.txt"
    translated_audio_path = "output_translated_audio.wav"
    final_video_path = "output_video.mp4"
    audio_path = 'og_audio.wav'
    # Execute each step sequentially
    extract_audio(video_path, audio_path)
    audio_to_text(audio_path, text_path)
    translate_text(text_path, translated_text_path, target_language=lang)
    text_to_speech(translated_text_path, translated_audio_path, language_code=lang)
    merge_audio_to_video(video_path, translated_audio_path, final_video_path)

    print("Video conversion completed successfully!")