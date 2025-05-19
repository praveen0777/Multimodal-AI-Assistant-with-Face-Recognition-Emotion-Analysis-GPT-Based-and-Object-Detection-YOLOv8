import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening (V key held)...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=8)
            command = r.recognize_google(audio)
            return command
        except sr.WaitTimeoutError:
            print("⏱️ Timeout: No speech detected.")
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""
