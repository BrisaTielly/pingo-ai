from decimal import Decimal

from expense_extractor import extract_expense
from transaction_repository import save_transaction
from whatsapp_sender import send_message


def process_message(payload: dict, client, api_key: str, phone_number_id: str) -> None:
    body = payload["message"]["text"]["body"]
    recipient = payload["message"]["from"]
    response = extract_expense(body, client)
    response_text = f"R$ {response.amount:.2f} - {response.description}"
    save_transaction(Decimal(str(response.amount)), response.description, recipient)
    send_message(recipient, response_text, api_key, phone_number_id)
