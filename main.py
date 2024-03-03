from generatetext import generate_and_save_response
from textseperator import read_novel_data
from generateaudio import save_audio
from generateimage import generate_image,download_image
from generatevideo import create_video
import os

def generate_video(prompt):

    if(prompt==""):
        print("ERROR : Input Was Null !! ")
        return
    try:
        #Text Gen
        response = generate_and_save_response(prompt)
        print(response)

        #Text Parser
        result = read_novel_data(response)
        print(result)

        #Audio Gen
        audio_path = save_audio(result[2],result[0])

        #Image Gen
        title = result[0]
        for prompt in result[3]:
            print(prompt)
            image_url = generate_image(prompt)
            download_image(image_url, title , prompt)

        #Video Gen
        images_dir = os.path.join(os.getcwd(), 'output', 'images', title)
        video_path = create_video(images_dir,audio_path,title)
        return video_path
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    prompt = input(">:")
    generate_video(prompt)

if __name__ == "__main__":
    main()