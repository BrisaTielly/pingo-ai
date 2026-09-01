from decimal import Decimal

from sqlalchemy.orm import Session

from database import engine
from models import Transaction


def save_transaction(amount: Decimal, description: str, phone_number: str) -> None:
    with Session(engine) as session:
        transaction = Transaction(
            amount=amount,
            description=description,
            phone_number=phone_number
        )
        session.add(transaction)
        session.commit()
