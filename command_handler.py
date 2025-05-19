import re
import datetime
import webbrowser
import pyjokes

from utils.weather_api import get_weather
from utils.reminder import set_reminder
from utils.gpt import ask_gpt
from utils.emotion_recognition import detect_emotion
from utils.web_search import web_search
from utils.object_detection import detect_objects  
from memory_module import update_memory, retrieve_memory, load_memory

def handle_command(command, user):
    command = command.lower()

    #  Memory teaching
    memory_patterns = [
        r"my name is (.+)",
        r"i am (.+)",
        r"i live in (.+)",
        r"i work at (.+)",
        r"i like (.+)",
        r"i love (.+)",
        r"my favorite (.+) is (.+)"
    ]
    for pattern in memory_patterns:
        match = re.search(pattern, command)
        if match:
            if "favorite" in pattern:
                key = f"favorite {match.group(1).strip()}"
                value = match.group(2).strip()
            else:
                key = pattern.split(" ")[1].replace("is", "").strip()
                value = match.group(1).strip()
            update_memory("user", key, value)
            return f"Got it! I’ll remember your {key} is {value}."

    #  Recall memory
    if "what do you know about me" in command:
        memory_data = load_memory()
        if memory_data:
            facts = [f"- {k}: {v}" for k, v in memory_data.items()]
            return "Here’s what I remember:\n" + "\n".join(facts)
        else:
            return "I don't have any memory about you yet."

    if "what is my" in command:
        match = re.search(r"what is my (.+)", command)
        if match:
            key = match.group(1).strip()
            value = load_memory().get(key)
            return f"You told me your {key} is {value}." if value else f"I don't know your {key} yet."

    #  Reminder
    if "remind me" in command:
        match = re.search(r"remind me to (.+) in (\d+) (minute|minutes|hour|hours)", command)
        if match:
            task = match.group(1).strip()
            time_amount = int(match.group(2))
            if "hour" in match.group(3):
                time_amount *= 60
            set_reminder(task, time_amount)
            return f"Reminder set to {task} in {time_amount} minutes."
        else:
            return "What should I remind you to do, and when?"

    #  Emotion detection
    if "how am i feeling" in command or "analyze my emotion" in command or "my mood" in command:
        emotion = detect_emotion()
        return f"You appear to be feeling {emotion.lower()}."

    #  Object detection 
    if "object detection" in command or "see surroundings" in command:
        detect_objects()
        return "Object detection stopped."

    #  Built-in commands
    if "time" in command:
        return datetime.datetime.now().strftime("The time is %I:%M %p")
    if "joke" in command:
        return pyjokes.get_joke()
    if "weather" in command:
        return get_weather("New York")
    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube..."

    #  GPT + Web fallback
    try:
        memory_data = load_memory()
        memory_str = "\n".join([f"{k}: {v}" for k, v in memory_data.items()]) if memory_data else ""
        return ask_gpt(command, memory_str)
    except Exception:
        print("⚠️ GPT failed. Falling back to web search.")
        return web_search(command)
