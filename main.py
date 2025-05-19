import time
import keyboard
from utils.stt import listen
from utils.tts import speak, stop_speaking
from command_handler import handle_command
from user_recognition import recognize_user
from utils.reminder import start_reminder_loop

def main():
    user = recognize_user()
    print(f"👋 Welcome back, {user}!")
    speak(f"Welcome back, {user}!", interrupt=False)  

    start_reminder_loop()

    print("✅ Maya is ready. Press V to speak.")
    speak("Maya is ready. Press V to speak.", interrupt=False)

    while True:
        if keyboard.is_pressed('v'):
            stop_speaking()
            print("🎤 Listening (V key held)...")
            command = listen()

            if not command.strip():
                speak("I didn't catch that. Try again.")
                continue

            print(f"🗣️ You said: {command}")
            if "exit" in command.lower() or "stop" in command.lower():
                speak("Goodbye!")
                break

            response = handle_command(command, user)
            print(f"🤖 Maya: {response}")
            speak(response)

        time.sleep(0.1)

if __name__ == "__main__":
    main()
