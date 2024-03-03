import requests
import os
from datetime import datetime
from openai import OpenAI
client = OpenAI(api_key=open('private/api_key.txt').read().strip('\n'))
from textseperator import read_novel_data

def download_image(url, title="Untitled" ,filename="Filename"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            # Get the file extension from the URL and clip it to '?' characters
            file_extension = url.split('?')[0].split('.')[-1][:3]  # Clipping file extension to '?' characters
            # Combine filename, timestamp, and file extension
            save_filename = f"{filename[:50]}_{timestamp}.{file_extension}"
            # Define folder paths
            current_directory = os.path.dirname(os.path.abspath(__file__))
            output_folder = os.path.join(current_directory, 'output', 'images', title )
            # Create folders if they don't exist
            os.makedirs(output_folder, exist_ok=True)
            # Save the image to the output/images folder
            save_path = os.path.join(output_folder, save_filename)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Image saved successfully as '{save_filename}' in the '{save_path}' directory.")
        else:
            print("Failed to download the image. Invalid URL or response status code.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def generate_image(prompt):
    prompt_add = "I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS:" + prompt
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_add,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        print(response)
        print("==============================================================")
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"An error occurred while generating the image: {str(e)}")

if __name__ == "__main__":
    text = open('output/text/naruto and hinata_2024-03-03_16-31-39.txt').read()
    parsed_data = read_novel_data(text)
    title = parsed_data[0]
    for prompt in parsed_data[3]:
        print(prompt)
        image_url = generate_image(prompt)
        download_image(image_url, title , prompt)  # Use prompt as filename