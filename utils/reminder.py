import schedule
import time
import threading
import datetime
from utils.tts import speak

reminders = []

def set_reminder(message, delay_minutes):
    remind_time = datetime.datetime.now() + datetime.timedelta(minutes=delay_minutes)
    formatted_time = remind_time.strftime("%H:%M")
    reminders.append((formatted_time, message))

    def job():
        speak(f"🔔 Reminder: {message}")
        schedule.clear(message)  # Remove after triggering

    schedule.every(delay_minutes).minutes.do(job).tag(message)
    speak(f"✅ Reminder set: I will remind you to {message} in {delay_minutes} minutes.")

def start_reminder_loop():
    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_schedule, daemon=True).start()
