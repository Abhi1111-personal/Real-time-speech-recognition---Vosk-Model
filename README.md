

This repository contains 6 files for demonstrating English or Hindi speech to text using VOSK:


These files contains the code for real-time speech recognition using VOSK. 

# English Speech to Text using VOSK
1. `English_realtime_speech_recognition.py`: 
It uses the `vosk` library to recognize speech from the microphone and print the recognized text to where cursor is pointed.

2. `terminal_English_Speech_To_Text.py`: 
simulate keyboard typing and paste the recognized text into the terminal.

3. `Doc_specific_English_STT.py`: 
simulate keyboard typing and paste the recognized text into the Specified document whose name is provided by the user in the code.


# Hindi Speech to Text using VOSK
4. `Hindi_realtime_speech_recognition.py`: 
It uses the `vosk` library to recognize speech from the microphone and print the recognized text to where cursor is pointed.

5. `terminal_Hindi_Speech_To_Text.py`:
simulate keyboard typing and paste the recognized text into the terminal.

6. `Doc_specific_Hindi_STT.py`: 
simulate keyboard typing and paste the recognized text into the Specified document whose name is provided by the user in the code.

# Vosk-Model (need to install)

7. `vosk-model-small-en-us-0.15.zip` and `vosk-model-small-hi-0.22.zip` are the model files for English and Hindi language respectively. These files are required for the speech recognition to work. Keep these files in the same folder as the program files OtherwiseChange the model path according to the requirement.

# Installation

To install and set up the Real-Time Hindi Speech-to-Text Transcription Tool on your local machine, please follow the steps below:

## Installation

1. **Clone the Repository:**

   Begin by cloning the repository to your local machine using Git. Open your terminal or command prompt and execute:

   ```bash
   git clone https://github.com/Abhi1111-personal/Real-time-speech-recognition---Vosk-Model.git
   ```

   This command will create a directory named `Real-time-speech-recognition---Vosk-Model` containing the project's files.

2. **Navigate to the Project Directory:**

   Change your current working directory to the project's root folder:

   ```bash
   cd Real-time-speech-recognition---Vosk-Model
   ```

3. **Download the Vosk Hindi Model:**

   The application utilizes the Vosk speech recognition toolkit with a specific model for Hindi. Download the pre-trained Hindi model from the [Vosk Model Repository](https://alphacephei.com/vosk/models).

   - **Download Link:** [vosk-model-small-hi-0.22](https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip)

   After downloading, extract the contents of the ZIP file into the project's root directory. Rename the extracted folder to `model` for consistency.

   Or You can use the provided two folder in the repo for the same purpose.

4. **Install packages**
    open your terminal, Navigate to the root file and install the following packages by running the following command in the terminal- 

    ```bash
   pip install pyautogui pynput sounddevice vosk
   ```

5. **Run the Application:**

   With all dependencies installed and the model in place, you can start the transcription tool:

   ```bash
   #python file_name.py
   #-----for example------
   python English_realtime_speech_recognition.py
   ```

   Ensure your microphone is connected and functioning properly. Once the application is running, it will begin capturing audio and transcribing Hindi speech in real-time.

## Usage

- **Typing Mode Toggle:**

  - Press the `F2` key to toggle typing mode on or off.
  - When typing mode is enabled, the transcribed text will be automatically typed into the currently active application where your cursor is focused.
  - Press `F2` again to disable typing mode.

- **Clipboard Integration:**

  - The application uses the system clipboard to handle Hindi text input, ensuring accurate representation of characters across different applications.

**Note:** Ensure that the target application where the text is being typed supports Hindi Unicode characters. Some applications may require specific font settings or language support to display Hindi text correctly.

By following these steps, you should have the Real-Time Hindi Speech-to-Text Transcription Tool installed and operational on your system. For any issues or further assistance, please refer to the project's [GitHub repository](https://github.com/Abhi1111-personal/Real-time-speech-recognition---Vosk-Model) or open an issue for support. 


