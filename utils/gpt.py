from openai import OpenAI
from dotenv import load_dotenv
import os

# Api key used
client = OpenAI(api_key="ADD YOUR GPT API KEY OVER HERE") #important

def ask_gpt(prompt, memory=None):
    system_prompt = "You are Maya, a helpful AI assistant created by Praveen. Answer naturally and supportively."

    if memory:
        prompt = f"Memory:\n{memory}\n\nUser: {prompt}"

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, I couldn't process that: {str(e)}"
