from abc import ABC, abstractmethod

from PaymentGateway.entities.PaymentRequest import PaymentRequest
from PaymentGateway.entities.PaymentResponse import PaymentResponse
from PaymentGateway.enums.PaymentEnum import PaymentStatus


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, request: PaymentRequest) -> PaymentResponse:
        pass


class AbstractPaymentProcessor(PaymentProcessor):
    MAX_RETRIES = 3

    def process_payment(self, request: PaymentRequest) -> PaymentResponse:
        for attempt in range(self.MAX_RETRIES):
            try:
                response = self.do_process(request)
                if response.status != PaymentStatus.FAILED:
                    return response
            except Exception as exc:
                print(f"Error processing payment: {exc}")

            if attempt < self.MAX_RETRIES - 1:
                print(f"Retrying payment attempt {attempt + 2} of {self.MAX_RETRIES}...")

        return PaymentResponse(PaymentStatus.FAILED, "Payment failed after retries")

    @abstractmethod
    def do_process(self, request: PaymentRequest) -> PaymentResponse:
        pass


class CreditCardPaymentProcessor(AbstractPaymentProcessor):
    def do_process(self, request: PaymentRequest) -> PaymentResponse:
        print(f"Processing credit card payment for amount: {request.amount} {request.currency}")
        return PaymentResponse(PaymentStatus.COMPLETED, "Credit card payment successful")


class PayPalPaymentProcessor(AbstractPaymentProcessor):
    def do_process(self, request: PaymentRequest) -> PaymentResponse:
        print(f"Processing PayPal payment for amount: {request.amount} {request.currency}")
        return PaymentResponse(PaymentStatus.COMPLETED, "PayPal payment successful")


class BankTransferPaymentProcessor(AbstractPaymentProcessor):
    def do_process(self, request: PaymentRequest) -> PaymentResponse:
        print(f"Processing bank transfer payment for amount: {request.amount} {request.currency}")
        return PaymentResponse(PaymentStatus.COMPLETED, "Bank transfer payment successful")

