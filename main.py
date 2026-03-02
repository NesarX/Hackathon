main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 1. PASTE YOUR KEY HERE ---
genai.configure(api_key="AIzaSyAbkLyA8TPq5BIhLGqH-ruthKNmLsJOSAw")

# Turn-based instructions for the AI
SYSTEM_PROMPT = (
    "You are the 'Stress Beast.' You must follow this EXACT 4-turn sequence: "
    "Turn 1: Ask about their day. "
    "Turn 2: Ask for the single hardest moment of their week. "
    "Turn 3: Tell a short, random, cheesy stress-relief joke, THEN ask for their 3 favorite songs. "
    "Turn 4: Suggest they listen to 'Weightless' by Marconi Union to finish the healing. "
    "Keep responses under 25 words and stay in character."
)

# --- 2. THE 2026 MODEL FIX ---
# gemini-1.5-flash is often retired/moved to v1. Use 2.5 for stability in 2026.
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", 
    system_instruction=SYSTEM_PROMPT
)

game_state = {"turn": 0, "history": []}

@app.get("/trigger-intervention")
async def trigger_intervention(user_voice_text: str):
    global game_state
    
    # Auto-reset after 4 turns
    if game_state["turn"] >= 4:
        game_state["turn"] = 0
        game_state["history"] = []

    game_state["turn"] += 1
    
    try:
        chat = model.start_chat(history=game_state["history"])
        response = chat.send_message(user_voice_text)
        
        game_state["history"].append({"role": "user", "parts": [user_voice_text]})
        game_state["history"].append({"role": "model", "parts": [response.text]})

        # Health bar: 100 -> 75 -> 50 -> 25 -> 0
        hp_map = {1: 75, 2: 50, 3: 25, 4: 0}
        current_hp = hp_map.get(game_state["turn"], 100)

        return {
            "boss_hp": current_hp,
            "reply_text": response.text,
            "message": f"PHASE {game_state['turn']}/4",
            "is_final": current_hp == 0
        }
    except Exception as e:
        print(f"--- ACTUAL ERROR: {e} ---")
        return {"reply_text": "Arena stabilizing... check terminal.", "boss_hp": 100}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
