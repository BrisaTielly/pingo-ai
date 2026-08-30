from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import NUMERIC, DateTime, func
from decimal import Decimal
from datetime import datetime

class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[Decimal] = mapped_column(NUMERIC(precision=10, scale=2), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())