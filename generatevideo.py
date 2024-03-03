from moviepy.editor import VideoClip, AudioFileClip, ImageSequenceClip
from textseperator import read_novel_data
import os

def create_video(images_dir, audio_file, title):
    # Get all image files in the directory
    image_files = sorted([os.path.join(images_dir, f) for f in os.listdir(images_dir) if f.endswith('.png')])
    num_images = len(image_files)

    # Load audio file
    audio_clip = AudioFileClip(audio_file)
    audio_duration = audio_clip.duration

    # Calculate fps dynamically
    fps = num_images / audio_duration

    # Create image sequence clip
    image_clip = ImageSequenceClip(image_files, fps=fps)

    # Set audio for the video clip
    video_clip = image_clip.set_audio(audio_clip)

    # Write the video file
    output_path = os.path.join(os.getcwd(), 'output', 'video')  # Adjust output path as needed
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path,f'{title}.mp4')
    video_clip.write_videofile(file_path, codec='libx264', audio_codec='aac')

    print(f"Video created successfully at {file_path}")
    return file_path

if __name__ == "__main__":
    text = open('output/text/Blooming Love_2024-03-03_16-31-39.txt').read()
    parsed_data = read_novel_data(text)
    title = parsed_data[0]
    images_dir = os.path.join(os.getcwd(), 'output', 'images',title)  # Path to the directory containing images
    audio_file = os.path.join(os.getcwd(), 'output', 'audio',' Blooming Love_2024-03-03_17-12-16.mp3')  # Path to the audio file
    create_video(images_dir, audio_file, title)
