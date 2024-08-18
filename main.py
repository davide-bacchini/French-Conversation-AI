from resources.french import conversation

encoding = "utf-8"

# Modify the prompt based on the experience you want with your teacher
messages = [
    {
        "role": "system",
        "content": "You are a French teacher. Your objective is to conversate with me. Don't be repetitive. The answer has to be only in french. Provide it without words from other languages.",
    },
]

freq = 44100

# Put how much time you want to speak
duration = 2

# How many conversation you want to do
n = 10

for i in range(n):
    conversation(messages, freq, duration)
