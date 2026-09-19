

from PaymentGateway.entities.PaymentRequest import PaymentRequest
from PaymentGateway.entities.Transaction import Transaction
from PaymentGateway.enums.PaymentEnum import PaymentStatus
from PaymentGateway.factory.PaymentProcessorFactory import PaymentProcessorFactory
import threading
class PaymentGatewayService:

    def __init__(self):
        self._observers = []
        self._processed : dict[str,Transaction] = {}
        self._lock = threading.Lock()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, transaction):
        for observer in self._observers:
            observer.on_payment_success(transaction)

    def update_payment_status(self,transaction,status):
        transaction.set_status(status)
        self.notify_observers(transaction)

    def process_payment(self, request: PaymentRequest):
        idmempotency_key = request.idempotency_key
        with self._lock:
            if idmempotency_key in self._processed:
                return self._processed[idmempotency_key]
            
        transaction = Transaction(request)
        self._processed[idmempotency_key] = transaction
        try:
            processor = PaymentProcessorFactory.get_payment_processor(request.payment_method)
            response = processor.process_payment(request)
            self.update_payment_status(transaction, response.status)

        except Exception as e:
            print(f"Error processing payment: {e}")
            self.update_payment_status(transaction, PaymentStatus.FAILED)

        return transaction
    