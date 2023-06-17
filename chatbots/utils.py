import openai
from django.conf import settings
from decouple import config

openai.api_key = config("API_KEY")


def chat_openai_helper_function(message, max_tokens=2000):
    try:
        if len(message.split()) > max_tokens:
            raise ValueError(
                "Your message is too long. Please reduce the length of your message."
            )

        prompt = message
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt[:4096],
            temperature=0.7,
            max_tokens=max_tokens,
        )
        return response.choices[0].text

    except Exception as e:
        # Handle any unexpected errors
        print("Error:", e)
        raise ValueError("An error occurred while processing the message.")
