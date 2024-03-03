import os
from datetime import datetime
from openai import OpenAI

def save_text_to_file(prompt, filename):
    try:
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Combine filename, timestamp, and file extension
        save_filename = f"{filename}_{timestamp}.txt"
        # Define folder paths
        output_folder = os.path.join(os.getcwd(), 'output', 'text')
        # Create folders if they don't exist
        os.makedirs(output_folder, exist_ok=True)
        # Save the text to the output/text folder
        save_path = os.path.join(output_folder, save_filename)

        with open(save_path, 'w') as file:
            file.write(prompt)

        print(f"Text saved successfully as '{save_filename}' in the '{save_path}' directory.")
        return save_path
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def generate_and_save_response(user_prompt):
    # Load OpenAI API key from file
    api_key = open('private/api_key.txt').read().strip('\n')
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Define message history
    message_history = [
        {"role": "user", "content": "You are a Novel writer in 600 words , write a Title and chapter name in first line then the text of the novel if my next prompt is from a copyrighted material do not mention names directly but create the scene then Give a 10 image scene prompts to generate image related to novel you wrote, If understood say 'OK'"}
    ]
    message_history.append({"role": "assistant", "content": "OK"})
    message_history.append({"role": "user", "content": user_prompt})

    # Get response from OpenAI GPT-3.5 model
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    response = completion.choices[0].message.content
    title_index = response.find("Title:") + len("Title:")
    title = response[title_index:response.find("\n", title_index)].replace('"', '')
    save_text_to_file(response, title)
    return response

def main():
    
    # User prompt input
    user_prompt = input(">: ")
    try:
        response = generate_and_save_response(user_prompt)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
