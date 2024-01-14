# Speech_to_text-Text_to_speech

1.Overview <br>
    Welcome to the Speech Converter application, a Python program that allows users to convert speech to text and text to speech. This application utilizes the Tkinter library for the graphical user       interface, SpeechRecognition for speech-to-text conversion, and gTTS (Google Text-to-Speech) for text-to-speech conversion.<br>
2.Features<br>
  Speech to Text Conversion: Press 'a' to initiate speech-to-text conversion. Users can speak into the microphone, and the application will convert the speech to text.<br>
  Text to Speech Conversion: Press 'b' to initiate text-to-speech conversion. Users can enter text, and the application will convert it to speech, playing the generated audio.<br>
3.Prerequisites<br>
  Make sure you have the following libraries installed before running the application:<br>
  1.tkinter<br>
  2.speech_recognition<br>
  3.gtts<br>
  You can install them using the following commands:<br>
      pip install tk<br>
      pip install SpeechRecognition<br>
      pip install gtts<br>
4.Usage<br>
  Run the script by executing the following command:<br>
        python script_name.py<br>
        
  The main window will appear with options to choose between speech-to-text and text-to-speech conversion.<br>

 a. If speech-to-text is selected:<br>
          Choose the language from the dropdown menu.<br>
          Click "Speak Now" to start the speech-to-text conversion.<br>
          The result will be displayed in a pop-up dialog.<br>
 b. If text-to-speech is selected:<br>
          Enter the text in the provided entry field.<br>
          Click "Submit" to start the text-to-speech conversion.<br>
          The generated audio will be played.<br>
          Supported Languages<br>
          English ('en')<br>
          Hindi ('hi')<br>
          Punjabi ('pa_IN')<br>
          Gujarati ('gu')<br>
          Bengali ('bn')<br>
  Note<br>
  The application creates a file named "text.txt" for speech-to-text conversion. Make sure to handle this file as needed.<br>

  For text-to-speech conversion, an MP3 file named "text.mp3" is generated and played. Ensure your system supports audio playback.<br>

5.Troubleshooting<br>
  If you encounter any issues during speech-to-text or text-to-speech conversion, error messages will be displayed in pop-up dialogs.<br>
  Feel free to contribute, report issues, or suggest improvements!






