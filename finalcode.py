# Importing necessary libraries
import tkinter as tk  # Tkinter is the standard GUI toolkit for Python
from tkinter import ttk, messagebox  # ttk provides themed Tkinter widgets, messagebox for displaying pop-up messages
import speech_recognition as sr  # Speech recognition library
from gtts import gTTS  # Google Text-to-Speech library
import os  # Operating system interface for file operations

# Defining the main application class
class ConvertSpeech:
    
    # Initializing the application
    # special function in python like constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Converter")
        self.root.geometry("550x250")

        self.First_choice = tk.StringVar()  # Variable to store user's choice
        self.language_choice = tk.StringVar()  # Variable to store selected language

        self.recognizer = sr.Recognizer()  # Speech recognition object

        # Creating GUI elements
        ttk.Label(root, text="Welcome to Speech_To_Text and Text_To_Speech conversion software", font=('Helvetica', 13)).pack(pady=15)
        ttk.Label(root, text="1. To convert speech to text press -> a \n2. To convert text to speech press -> b", font=('Helvetica', 11)).pack(pady=10)
        ttk_combobox = ttk.Combobox(self.root, textvariable=self.First_choice, values=['a','b'])
        ttk_combobox.pack(pady=10)
        ttk.Button(root, text="Submit", command=self.process_choice).pack(pady=10)

    # Handling user's choice
    def process_choice(self):
        choice = self.First_choice.get()
        if choice == 'a':
            self.select_language_for_speech_to_text_conversion()
        elif choice == 'b':
            self.text_to_speech()
        else:
            messagebox.showerror("Error", "Invalid choice entered")

    # Selecting language for speech-to-text conversion
    def select_language_for_speech_to_text_conversion(self):
        language_dialog = tk.Toplevel(self.root)
        language_dialog.title("Select Language")
        language_dialog.geometry("300x300")

        ttk.Label(language_dialog, text="Select the language you are going to speak :",font=('Helvetica', 10)).pack(pady=10)
        ttk.Label(language_dialog, text="English-->'en'\nHindi-->'hi'\nPunjabi->'pa_IN'\nGujarati-->'gu'\nBengali-->'bn'",font=('Helvetica', 10)).pack(pady=10)

        # Combobox for language selection
        language_combobox = ttk.Combobox(language_dialog, textvariable=self.language_choice, values=["en", "hi", "pa_IN", "gu", "bn"])
        language_combobox.pack(pady=10)

        ttk.Button(language_dialog, text="Speak Now", command=self.speech_to_text).pack(pady=10)

    # Displaying result in a pop-up dialog
    def show_result(self, message):
        result_dialog = tk.Toplevel(self.root)
        result_dialog.title("Result")
        ttk.Label(result_dialog, text=message,font=('Helvetica', 10)).pack(pady=10)

    # Performing speech-to-text conversion
    def speech_to_text(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source)
                print("Speak anything:")
                audio = self.recognizer.listen(source)
                print("Recognizing Now......")
                text = self.recognizer.recognize_google(audio, language=self.language_choice.get())
                print("Done")
                self.show_result("Speech converted to text successfully\nYou have said : " + text)
        except sr.UnknownValueError:
            self.show_error("Sorry, could not understand the audio")
        except sr.RequestError as e:
            self.show_error("Could not request results from Google Speech Recognition service")
        with open("text.txt", "w", encoding="utf-8") as file:
            file.write(text)

    # Handling text-to-speech conversion
    def text_to_speech(self):
        text_input_dialog = tk.Toplevel(self.root)
        text_input_dialog.title("Text Input")
        text_input_dialog.geometry("300x150")

        ttk.Label(text_input_dialog, text="Enter the text for text-to-speech:").pack(pady=10)

        # Entry widget for text input
        text_entry = ttk.Entry(text_input_dialog, textvariable=tk.StringVar())
        text_entry.pack(pady=10)

        # Button to submit text for conversion
        submit_button = ttk.Button(text_input_dialog, text="Submit", command=lambda: self.text_to_speech_action(text_entry.get()))
        submit_button.pack(pady=10)

    # Performing the text-to-speech conversion action
    def text_to_speech_action(self, input_text):
        if input_text:
            # Using Google Text-to-Speech to convert text to speech
            tts = gTTS(input_text, lang='hi', slow=False)
            tts.save("text.mp3")
            os.system("start text.mp3")
        else:
            self.show_error("No text to convert to speech.")

    # Displaying error messages in a pop-up
    def show_error(self, message):
        messagebox.showerror("Error", message)

# Main execution when the script is run
if __name__ == "__main__":
    #creating the main window or first window which appears after code executes
    root = tk.Tk()
    # instanticiation of convertspeech class 
    app = ConvertSpeech(root)
    #starting the tinker event loop
    root.mainloop()