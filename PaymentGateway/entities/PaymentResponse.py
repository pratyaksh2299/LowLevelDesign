from abc import ABC,abstractmethod
from PaymentGateway.enums.PaymentEnum import PaymentStatus, PaymentMethod

class PaymentResponse(ABC):
    def __init__(self,status:PaymentStatus,message:str):
        self._status = status
        self._message = message

    @property
    def status(self):
        return self._status

    @property
    def message(self):
        return self._message