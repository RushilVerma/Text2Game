def read_novel_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return read_novel_data(data)

def read_novel_data(data):

    # Split the data into title, chapter title, and text
    title_index = data.find("Title:") + len("Title:")
    title = data[title_index:data.find("\n", title_index)].replace('"', '').replace(":"," ")
    title = title[1:]
    chapter_title_index = data.find("Chapter") + len("Chapter")
    chapter_title = data[chapter_title_index:data.find("\n", chapter_title_index)].strip()

    chapter_text_index = data.find(chapter_title) + len(chapter_title)
    chapter_text = data[chapter_text_index:data.find("Image prompts:")].strip()

    # Split the data into image prompts
    image_prompts_text = data[data.find("Image prompts:") + len("Image prompts:"):].strip()
    image_prompts = [line.strip() for line in image_prompts_text.split("\n") if line.strip()]

    # Return the extracted data as an array
    return [title, chapter_title, chapter_text, image_prompts]

if __name__ == "__main__":
    # Example usage:
    filename = 'output/text/naruto and hinata_2024-03-03_16-31-39.txt'
    novel_data = read_novel_data(filename)
    print("Title:", novel_data[0])
    print("Chapter Title:", novel_data[1])
    print("Chapter Text:", novel_data[2])
    print("\nImage Prompts:")
    for i, prompt in enumerate(novel_data[3], start=1):
        print(f"{i}. {prompt}")
