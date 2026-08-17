import threading

class Order(threading.Thread):
    def __init__(self,oder_id :int , priority=1):
        super().__init__(name='thread_1')
        self.order_id = oder_id
        self.priority = priority

    def run(self):
        print(f'processing {self.order_id} with priority {self.priority}')


if __name__ == '__main__':

    order = Order(35345,5)
    order.start()
    order.join()