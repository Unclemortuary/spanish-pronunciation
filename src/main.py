import os  
from gtts import gTTS  

def generate_audio(word, index, lang='es'):  
    tts = gTTS(text=word, lang=lang)  
    filename = f"{index}.mp3"
    tts.save(filename)  
    print(f"Generated audio file: {filename}")  

def main():  
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'words.txt')

    with open(file_path, 'r') as file:
        words = file.read().split(",")
    for index, word in enumerate(words, start=1):
        word = word.strip()
        generate_audio(word, index)

if __name__ == "__main__":  
    main()  