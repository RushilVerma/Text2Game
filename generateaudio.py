import os
from datetime import datetime
import pyttsx3
from generatetext import generate_and_save_response
from textseperator import read_novel_data

def save_audio(text, title):
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Combine filename, timestamp, and file extension
        save_filename = f"{title[:50]}_{timestamp}.mp3"  # Clipping title to 50 characters
        # Define folder paths
        current_directory = os.path.dirname(os.path.abspath(__file__))
        output_folder = os.path.join(current_directory, 'output', 'audio')
        # Create folders if they don't exist
        os.makedirs(output_folder, exist_ok=True)
        # Save the audio to the output/audio folder
        save_path = os.path.join(output_folder, save_filename)

        # Convert text to speech and save it as an audio file using pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')  # Female voice
        engine.setProperty('voice', 'english')  # Use default English voice
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 50)  # Lower down the speed (words per minute)
        engine.save_to_file(text, save_path)
        engine.runAndWait()

        print(f"Audio saved successfully as '{save_filename}' in the '{save_path}' directory.")
        return save_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":

    text = open('output/text/naruto and hinata_2024-03-03_16-31-39.txt').read()
    parsed_data = read_novel_data(text)
    save_audio(parsed_data[2], parsed_data[0])