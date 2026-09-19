from abc import ABC,abstractmethod
import threading
from PaymentGateway.entities.PaymentRequest import PaymentRequest
import uuid

from PaymentGateway.enums.PaymentEnum import PaymentStatus
from datetime import datetime

class Transaction(ABC):

    def __init__(self,request:PaymentRequest):
        self._request = request
        self._transaction_id = str(uuid.uuid4())
        self._status = PaymentStatus.INITIATED
        self._timestamp = datetime.now()
        self._lock = threading.Lock()

    def set_status(self,status:PaymentStatus):
        with self._lock:    
            if self._status !=  status:
                self._status = status

    @property
    def transaction_id(self):
        return self._transaction_id

    @property
    def status(self):
        return self._status

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def request(self):
        return self._request