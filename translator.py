import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
from googletrans import Translator

def main():
    root = tk.Tk()
    root.title("Live Subtitles")
    preferred_language = tk.StringVar()
    language_options = ["Hindi", "Marathi", "Gujrati", "German", "French", "Spanish", "Korean"]
    language_menu = ttk.OptionMenu(root, preferred_language, language_options[0], *language_options)
    language_menu.pack(pady=10)

    def start_subtitles():
 
        language = preferred_language.get()
        recognizer = sr.Recognizer()
        translator = Translator()

        with sr.Microphone() as source:
            print("Listening for English audio... (Press Ctrl+C to stop)")
            while True:
                try:
                   
                    audio = recognizer.listen(source)
                    english_text = recognizer.recognize_google(audio)
                    print(f"Recognized English Text: {english_text}")
                    if language == "Hindi":
                        translated_text = translator.translate(english_text, dest='hi').text
                    elif language == "Marathi":
                        translated_text = translator.translate(english_text, dest='mr').text
                    elif language == "Gujrati":
                        translated_text = translator.translate(english_text, dest='gu').text
                    elif language == "German":
                        translated_text = translator.translate(english_text, dest='de').text
                    elif language == "French":
                        translated_text = translator.translate(english_text, dest='fr').text
                    elif language == "Spanish":
                        translated_text = translator.translate(english_text, dest='es').text
                    elif language == "Korean":
                        translated_text = translator.translate(english_text, dest='ko').text

                    print(f"{language} Subtitles: {translated_text}")

                except (sr.UnknownValueError, sr.RequestError):
                    print("Could not understand the audio or request failed.")
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
    start_button = tk.Button(root, text="Start Subtitles", command=start_subtitles)
    start_button.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()