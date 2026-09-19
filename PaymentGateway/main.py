import os
import sys

if __package__ in (None, ""):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PaymentGateway.PaymentGatewayService import PaymentGatewayService
from PaymentGateway.entities.PaymentRequest import PaymentRequest
from PaymentGateway.enums.PaymentEnum import PaymentMethod
from PaymentGateway.observer.PaymentObservers import MerchantObserver, UserObserver


if __name__ == "__main__":
    service = PaymentGatewayService()
    service.add_observer(MerchantObserver())
    service.add_observer(UserObserver())

    request = PaymentRequest(
        amount=250.50,
        currency="USD",
        payment_method=PaymentMethod.CREDIT_CARD,
        idempotency_key="pay-001",
        payer_id="payer-123",
    )

    transaction = service.process_payment(request)
    print(f"Transaction ID: {transaction.transaction_id}")
    print(f"Status: {transaction.status.value}")
    print(f"Message: {transaction.request.payment_method.value}")


