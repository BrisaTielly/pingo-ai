import os
from fastapi import FastAPI, Query, HTTPException, Response
from dotenv import load_dotenv
from google import genai
from expense_extractor import extract_expense

load_dotenv()

expected_verify_token = os.getenv("WEBHOOK_VERIFY_TOKEN")

client = genai.Client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/webhook")
def read_webhook(challenge: str = Query(alias="hub.challenge"), mode: str = Query(alias="hub.mode"), verify_token: str = Query(alias="hub.verify_token")):
    if mode == "subscribe" and verify_token == expected_verify_token:
        return Response(content=challenge, media_type="text/plain")

    raise HTTPException(status_code=403, detail="Verificação Inválida")

@app.post("/webhook")
def receive_webhook(payload: dict):
    body = payload["message"]["text"]["body"]
    response = extract_expense(body, client)
    print(response)
    return response

