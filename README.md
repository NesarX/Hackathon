Gemini Inner Arena: The Stress Beast
An interactive, voice-controlled emotional regulation "boss fight." Using Google Gemini 2.5/3.0, this application challenges users to "defeat" their stress through a 4-phase guided conversation.

Featuring a Glitch UI, real-time speech-to-text, and a dynamic "Health Bar" that drains as you process your day.

🚀 Features
Voice-Driven Combat: Hold the microphone to "attack" the Beast with your thoughts.

Glitch UI: The "Eye of Gemini" physically glitches and shakes when receiving voice input.

4-Phase Logic:

Venting: Share the weight of your day.

Focus: Pinpoint the single hardest moment.

Humor: The Beast attempts to "break" your stress with a random joke.

Remedy: Final transformation and relaxation music suggestion.

Automated Reset: The Arena clears and resets state automatically after the final phase.

🛠️ Installation
1. Prerequisites
Python 3.9+

A Google Gemini API Key from Google AI Studio

A modern browser (Chrome is recommended for SpeechRecognition support)

2. Backend Setup
Bash
# Install dependencies
pip install -U google-generativeai fastapi uvicorn
3. Configuration
Open main.py and insert your API key:

Python
genai.configure(api_key="YOUR_AIZA_KEY_HERE")
🎮 How to Play
Start the Brain:

Bash
python main.py
Start the Arena (Frontend):
In a new terminal window:

Bash
python -m http.server 8080
Enter the Arena:
Open http://localhost:8080 in your browser.

The Fight:

Hold the Spacebar/Mic Button to speak.

Watch the Health Bar drop as you move through the phases.

Listen to the Beast's responses (ensure your volume is up!).
