import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 170)

tts_thread = None
is_talking = False
lock = threading.Lock()

def speak(text, interrupt=True):
    global tts_thread, is_talking

    def run():
        global is_talking
        with lock:
            is_talking = True
            try:
                engine.say(text)
                engine.runAndWait()
            except RuntimeError as e:
                print("[TTS Error]", e)
            is_talking = False

    if interrupt:
        stop_speaking()

    tts_thread = threading.Thread(target=run)
    tts_thread.start()

def stop_speaking():
    global tts_thread, is_talking
    if engine._inLoop:
        engine.endLoop()
    engine.stop()
    is_talking = False
    if tts_thread and tts_thread.is_alive():
        tts_thread.join(timeout=0.1)

def is_speaking():
    global is_talking
    return is_talking
