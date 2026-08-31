from pydantic import BaseModel
from decimal import Decimal

class ExpenseExtraction(BaseModel):
    amount: Decimal | None
    description: str | None
    needs_confirmation: bool

def extract_expense(message: str, client) -> ExpenseExtraction:
    prompt = f"Você é um extrator de gastos, deve extrair da mensagem recebida o valor, descricao e se precisa de confirmação, responde somente em JSON com as informações absorvidas, valores são passados como número, sem `R$` e campos ausentes na mensagem devem ser registrados como null, é proibido fazer adivinhação. Aqui está a mensagem recebida: {message}"

    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt,
        response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": ExpenseExtraction.model_json_schema()
    },
    )
    expense_extraction = ExpenseExtraction.model_validate_json(interaction.output_text)
    return expense_extraction