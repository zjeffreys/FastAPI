from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

class ChatMessage(BaseModel):
    message: str

@app.post("/getChatResponse")
def get_chat_response(message: ChatMessage):
    # Send the user's message to GPT-3.5 and get a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message.message,
        max_tokens=50,  # Adjust as needed
    )
    
    return {"response": response.choices[0].text.strip()}
