from PaymentGateway.enums.PaymentEnum import PaymentMethod
from PaymentGateway.PaymentProcessor import (
    BankTransferPaymentProcessor,
    CreditCardPaymentProcessor,
    PayPalPaymentProcessor,
)


class PaymentProcessorFactory:

    @staticmethod
    def get_payment_processor(payment_method: PaymentMethod):
        if payment_method == PaymentMethod.CREDIT_CARD:
            return CreditCardPaymentProcessor()
        if payment_method == PaymentMethod.PAYPAL:
            return PayPalPaymentProcessor()
        if payment_method == PaymentMethod.BANK_TRANSFER:
            return BankTransferPaymentProcessor()

        raise ValueError(f"Unsupported payment method: {payment_method}")