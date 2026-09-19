from abc import ABC, abstractmethod
from PaymentGateway.enums.PaymentEnum import PaymentStatus, PaymentMethod
class PaymentRequest(ABC):

    def __init__(self, amount, currency, payment_method, idempotency_key, payer_id):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        self._amount = amount
        self._currency = currency
        self._payment_method = payment_method
        if not idempotency_key:
            raise ValueError("Idempotency key cannot be empty")
        self._idempotency_key = idempotency_key
        if not payer_id:
            raise ValueError("Payer ID cannot be empty")
        self._payer_id = payer_id

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @property
    def payment_method(self):
        return self._payment_method

    @property
    def idempotency_key(self):
        return self._idempotency_key

    @property
    def payer_id(self):
        return self._payer_id
