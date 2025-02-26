import sounddevice as sd
import queue
import sys
import json
import pyautogui
import keyboard
from vosk import Model, KaldiRecognizer

# Step 1: Load the Hindi Model
model_path = "vosk-model-small-en-us-0.15"
model = Model(model_path)

# Step 2: Set Up the Audio Queue
audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    """Capture audio from the microphone and add it to the queue."""
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

# Step 3: Type Text into Any Application
def type_text(text):
    """Simulate keyboard typing using pyautogui."""
    if text.strip():  # Type only if text is not empty
        pyautogui.write(text, interval=0.05)  # Simulate typing with a delay
        pyautogui.press('enter')  # Press Enter after each sentence

# Step 4: Real-time Speech-to-Text and Typing
def recognize_speech():
    """Continuously recognize and type speech in real-time."""
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("\n🎤 Listening... Speak into the microphone (Hindi). Press 'F2' to toggle typing.\n")
        rec = KaldiRecognizer(model, 16000)
        typing_enabled = False

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
                    type_text(text)  # Type into the active window

            else:
                partial_result = json.loads(rec.PartialResult())
                if partial_result.get("partial"):
                    print("Listening... " + partial_result["partial"], end="\r")

# Step 5: Start the Speech Recognition
if __name__ == "__main__":
    recognize_speech()
