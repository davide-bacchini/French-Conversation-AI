# French Conversation AI

This program helps users improve their French language skills by engaging in conversations with an **AI-powered** French teacher. It provides an interactive speaking and listening experience, allowing users to practice their French in a controlled environment.

## Features

- Speech recognition for user input using **OpenAI's Whisper model**
- AI-generated French responses using **Meta's LLAMA model**
- Text-to-speech output for listening practice
- Customizable conversation settings

## Key AI Components

This project leverages powerful AI models to create a realistic and helpful language learning experience:

- **LLAMA (Language Model for Dialogue Applications)**: An advanced language model developed by Meta, used here to generate contextually appropriate French responses.
- **Whisper**: OpenAI's robust speech recognition system, employed to accurately transcribe the user's spoken French input.

## Requirements

To run this program, you'll need Python and the following libraries:

```
groq==0.9.0
numpy==1.26.4
playsound==1.3.0
sounddevice==0.5.0
scipy==1.14.0
torch==2.3.1
transformers==4.44.0
wavio==0.0.9
```

You can install these dependencies using the provided `requirements.txt` file:

```
pip install -r requirements.txt
```

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies as mentioned above.
3. Set up your Groq API key:
   - Sign up for a Groq account and obtain an API key.
   - Set the `GROQ_API_KEY` environment variable with your API key.

## Usage

1. Run the main script:

```
python main.py
```

2. The program will start a conversation loop:
   - You'll be prompted to speak in French.
   - The AI will transcribe your speech using Whisper, generate a response with LLAMA, and speak it back to you.
   - This process repeats for the number of turns specified in `main.py`.

## Customization

You can customize various aspects of the conversation:

- In `main.py`:
  - Modify the `messages` list to change the AI teacher's personality or focus.
  - Adjust `duration` to change how long you can speak in each turn.
  - Change `n` to set the number of conversation turns.

## Components

- `main.py`: The main script that orchestrates the conversation.
- `french.py`: Handles speech recognition, text-to-speech, and conversation flow.
- `large_v3.py`: Contains the Whisper speech recognition model implementation.
- `LLAMA.py`: Manages the AI response generation using the LLAMA model via the Groq API.

## Note

This program requires a microphone for speech input and speakers or headphones for audio output. Ensure your system's audio devices are properly configured before running the program.
