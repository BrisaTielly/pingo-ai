import os

from dotenv import load_dotenv
from fastapi import FastAPI, Query, HTTPException, Response, BackgroundTasks
from google import genai

from expense_processor import process_message

load_dotenv()

expected_verify_token = os.getenv("WEBHOOK_VERIFY_TOKEN")
kapso_api_key = os.getenv("KAPSO_API_KEY")
kapso_phone_number_id = os.getenv("KAPSO_PHONE_NUMBER_ID")

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
def receive_webhook(payload: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_message, payload, client, kapso_api_key, kapso_phone_number_id)
    return {"status": "received"}
