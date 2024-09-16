# Text2Game

**Description:**

The "Text2Game" project is a Python-based tool that converts textual prompts into dynamic video slideshow novel stories. Utilizing natural language processing, multimedia editing, and automation, this project provides an engaging way to visualize narratives.

**Features:**

- **Textual Prompt Input:** Input textual prompts to create stories.
- **Automated Multimedia Creation:** Generates video slideshows from text.
- **Dynamic Synchronization:** Slides and audio are synchronized for a cohesive experience.
- **Customization Options:** Configure slide duration, transition effects, and audio settings.
- **Export Options:** Export the final video in various formats.

**Installation:**

Ensure you have Python installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```
Usage:

Run the Main Script: Execute the main.py script to start the program and provide a textual prompt when prompted.
bash
Copy code
python main.py
Provide Prompt: The script will generate and save a video based on the provided prompt.
File Structure:

generateaudio.py: Functions for creating audio from text.
generateimage.py: Functions for generating and downloading images.
generatetext.py: Functions for generating text responses.
generatevideo.py: Functions for creating the final video.
textseperator.py: Functions for parsing text data.
main.py: Main script for generating video from prompts.
main.ipynb: Jupyter notebook for running the main script interactively.
playbook.ipynb: Additional Jupyter notebook for experimentation or play.
requirements.txt: File listing project dependencies.
.gitignore: Specifies files and directories to be ignored by Git.
Customization:

Modify settings in the config.py (if available) to adjust video parameters like slide duration and effects.
Contributing:

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License:

This project is licensed under the MIT License. See the LICENSE file for details.

Contact:

For questions or feedback, reach out to Rushil Verma[https://github.com/RushilVerma].

Transform your textual prompts into captivating video slideshows with "Text2Game"!
