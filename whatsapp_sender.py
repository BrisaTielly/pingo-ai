import httpx


def send_message(recipient: str, text: str, api_key: str, phone_number_id: str) -> dict: 
    url = f"https://api.kapso.ai/meta/whatsapp/v24.0/{phone_number_id}/messages"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "text",
        "text": {
            "body": text
        }
    }
    response = httpx.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()