import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
import os

model = None
engine = None

def setup_tts():
    global engine
    if engine is None:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)  
        engine.setProperty('volume', 1.0)
    return engine

def load_model():
    global model
    if model is None:
        from faster_whisper import WhisperModel
        print("⚡ Loading AI model (one-time)...")
        model = WhisperModel(
            "base",              
            device="cuda",       
            device_index=0,     
            compute_type="float16"
        )
    return model

def record_audio(duration=3, fs=16000):
    print("\n🎤 Recording (3 sec)...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    wav.write(temp_file.name, fs, recording)
    return temp_file.name

def speech_to_text():
    model = load_model()
    audio_file = record_audio()

    print("⚡ Processing with GPU...")
    segments, info = model.transcribe(
        audio_file,
        language="en",     
        beam_size=1,       
        vad_filter=True    
    )

    text = " ".join([seg.text for seg in segments])
    print("🧠 Detected language:", info.language)
    print("🗣️ You said:", text)

    os.remove(audio_file)
    return text

def translate_text(text, target_language):
    from deep_translator import GoogleTranslator

    translated = GoogleTranslator(
        source='auto',   
        target=target_language
    ).translate(text)

    print("🌍 Translated:", translated)
    return translated

def choose_languages():
    print("\nChoose a language:")
    print("1. Spanish")
    print("2. German")
    print("3. French")

    choice = input("Enter choice: ")
    return {"1": "es", "2": "de", "3": "fr"}.get(choice, "hi")

def main():
    print("🚀 Ready instantly!")

    target_language = choose_languages()
    text = speech_to_text()

    if text:
        translated = translate_text(text, target_language)

        engine = setup_tts()

        print("🔊 Speaking...")
        engine.say(text)
        engine.say(translated)
        engine.runAndWait()

    print("✅ Done")

if __name__ == "__main__":
    while True:   
        main()