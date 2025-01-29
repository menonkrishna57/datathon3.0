import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os
import playsound

def get_word_meaning(word):
    url = f"https://www.dictionary.com/browse/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    meaning_div = soup.find('div', class_='css-1o58fj8 e1hk9ate0')
    if meaning_div:
        return meaning_div.text.strip()
    else:
        return "Meaning not found"

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    filename = "temp.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def main():
    while True:
        word = input("Enter word which u want to search (else: type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break
        meaning = get_word_meaning(word)
        print(f"Meaning of '{word}': {meaning}")

        if input("Do you want to hear the meaning? (Type: yes/no) ").strip().lower() == 'yes':
            speak_text(meaning)

if __name__ == "__main__":
    main()