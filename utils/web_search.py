import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# we are Loading .env file to get API key
load_dotenv()

def web_search(query):
    api_key = os.getenv("ADD YOUR SERPAPI KEY HERE") #important to make it work

    if not api_key:
        return "SerpAPI key not found. Please set it in your .env file."

    params = {
        "q": query,
        "hl": "en",
        "api_key": api_key
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        # This code will Try to extract from answer box
        if "answer_box" in results:
            box = results["answer_box"]
            return box.get("snippet") or box.get("answer") or box.get("definition")

        # Else fallback to organic snippet
        if "organic_results" in results and results["organic_results"]:
            return results["organic_results"][0].get("snippet", "No relevant info found.")

        return "No relevant information found on the web."

    except Exception as e:
        return f"Search failed: {str(e)}"
