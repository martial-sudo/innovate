import sys
from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio(video_path, output_audio_path):
    # Load the video clip
    video_clip = VideoFileClip(video_path)

    # Extract audio
    audio_clip = video_clip.audio

    # Save the audio file
    audio_clip.write_audiofile(output_audio_path)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python extract_audio.py <video_path> <output_audio_path>")
        sys.exit(1)

    # Extract command-line arguments
    video_path = sys.argv[1]
    output_audio_path = sys.argv[2]

    # Call extract_audio function with the provided arguments
    extract_audio(video_path, output_audio_path)
