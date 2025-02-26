# for using it on different applications
import sounddevice as sd
import queue
import sys
import json
import pyautogui
import pyperclip
import keyboard
import pygetwindow as gw
from vosk import Model, KaldiRecognizer
import time
# Load the Hindi Model
# model_path = "vosk-model-small-en-us-0.15"
model_path = "vosk-model-small-en-us-0.15"
model = Model(model_path)

# Set Up the Audio Queue
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    """Capture audio from the microphone and add it to the queue."""
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

def type_text(text):
    """Simulate keyboard typing using pyautogui."""
    if text.strip():  # Type only if text is not empty
        # pyautogui.write(text, interval=0.05)  # Simulate typing with a delay
        # pyautogui.write(text)  # Simulate typing without a delay
        pyperclip.copy(text)  # Copy text to clipboard
        pyautogui.hotkey('ctrl', 'v')  # Paste text
        pyperclip.copy('')  # Clear the clipboard

def activate_window(title):
    """Activate the window with the given title."""
    windows = gw.getWindowsWithTitle(title)
    if windows:
        window = windows[0]
        try:
            window.activate()
        except:
            window.minimize()
            window.maximize()
        time.sleep(0.5)  # Wait for the window to come to the foreground
        return True
    else:
        print(f"Window with title '{title}' not found.")
        return False

def recognize_speech():
    """Continuously recognize and type speech in real-time."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("\n🎤 Listening... Speak into the microphone (Hindi). Press 'F2' to toggle typing.\n")
        rec = KaldiRecognizer(model, 16000)
        typing_enabled = False
        target_window_title = "test1"  # Replace with your Word document's title

        while True:
            if keyboard.is_pressed('f2'):  # Toggle typing mode when F2 is pressed
                typing_enabled = not typing_enabled
                print("\n✍️ Typing Mode: " + ("ON" if typing_enabled else "OFF") + "\n")
                while keyboard.is_pressed('f2'):
                    pass  # Wait until key is released

            data = audio_queue.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result["text"]
                print("👉 You said (English):", text)
                if typing_enabled:
                    if activate_window(target_window_title):
                        type_text(text)  # Type into the active window
                    else:
                        print("Please open the target application and ensure the title matches.")

            else:
                partial_result = json.loads(rec.PartialResult())
                if partial_result.get("partial"):
                    print("Listening... " + partial_result["partial"], end="\r")

if __name__ == "__main__":
    recognize_speech()