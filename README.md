# Speech_to_text-Text_to_speech

1.Overview
    Welcome to the Speech Converter application, a Python program that allows users to convert speech to text and text to speech. This application utilizes the Tkinter library for the graphical user       interface, SpeechRecognition for speech-to-text conversion, and gTTS (Google Text-to-Speech) for text-to-speech conversion.

2.Features
  Speech to Text Conversion: Press 'a' to initiate speech-to-text conversion. Users can speak into the microphone, and the application will convert the speech to text.

  Text to Speech Conversion: Press 'b' to initiate text-to-speech conversion. Users can enter text, and the application will convert it to speech, playing the generated audio.

3.Prerequisites
  Make sure you have the following libraries installed before running the application:

  1.tkinter
  2.speech_recognition
  3.gtts
  You can install them using the following commands:
      pip install tk
      pip install SpeechRecognition
      pip install gtts
4.Usage
  Run the script by executing the following command:
        python script_name.py
        
  The main window will appear with options to choose between speech-to-text and text-to-speech conversion.

 a. If speech-to-text is selected:
          Choose the language from the dropdown menu.
          Click "Speak Now" to start the speech-to-text conversion.
          The result will be displayed in a pop-up dialog.
 b. If text-to-speech is selected:

          Enter the text in the provided entry field.
          Click "Submit" to start the text-to-speech conversion.
          The generated audio will be played.
          Supported Languages
          English ('en')
          Hindi ('hi')
          Punjabi ('pa_IN')
          Gujarati ('gu')
          Bengali ('bn')
  Note
  The application creates a file named "text.txt" for speech-to-text conversion. Make sure to handle this file as needed.

  For text-to-speech conversion, an MP3 file named "text.mp3" is generated and played. Ensure your system supports audio playback.

5.Troubleshooting
  If you encounter any issues during speech-to-text or text-to-speech conversion, error messages will be displayed in pop-up dialogs.
  Feel free to contribute, report issues, or suggest improvements!






