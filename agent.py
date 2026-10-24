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

    # Topic explanation
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
        Explain {topic} in simple beginner-friendly language.
        Give:
        1. A simple explanation
        2. Five key points
        3. A real-world example
        """
    )

    print("\nSTUDY NOTES\n")
    print(response.text)

    # Quiz mode
    quiz = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
        Create 3 multiple-choice quiz questions about {topic}.
        Give 4 options for each question.
        Do not show the answers yet.
        """
    )

    print("\nQUIZ\n")
    print(quiz.text)


if __name__ == "__main__":
    study_agent()
