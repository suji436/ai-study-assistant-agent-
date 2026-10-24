
import os
from google import genai

def study_agent():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("GEMINI_API_KEY is not configured.")
        return

    client = genai.Client(api_key=api_key)

    print("Welcome to AI Study Assistant!")
    topic = input("What topic do you want to learn? ")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=(
            f"Explain {topic} to a beginner. "
            "Give a simple explanation, key points, "
            "and three practice questions."
        )
    )

    print("\nYour study notes:\n")
    print(response.text)

if __name__ == "__main__":
    study_agent()
