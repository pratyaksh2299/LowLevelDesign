from abc import ABC, abstractmethod

from PaymentGateway.entities.Transaction import Transaction


class PaymentObserver(ABC):

    @abstractmethod
    def on_payment_success(self, transaction: Transaction):
        pass


PaymentObservere = PaymentObserver


class MerchantObserver(PaymentObserver):

    def on_payment_success(self, transaction: Transaction):
        print(f"Merchant notified: Payment successful for transaction {transaction.transaction_id} with status {transaction.status.value}")


class UserObserver(PaymentObserver):

    def on_payment_success(self, transaction: Transaction):
        print(f"User notified: Payment successful for transaction {transaction.transaction_id} with status {transaction.status.value}")

