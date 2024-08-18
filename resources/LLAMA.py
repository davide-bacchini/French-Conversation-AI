import os

from groq import Groq


api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)


def answer(prompt, messages, model="llama3-8b-8192"):
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=1
    )
    messages.append({"role": "system", "content": response.choices[0].message.content})
    return response.choices[0].message.content
