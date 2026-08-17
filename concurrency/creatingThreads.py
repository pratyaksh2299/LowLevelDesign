import threading
import time
def process_order(order_id , priority=1):
    print(f"Processing order {order_id} with priority {priority}")


if __name__ == '__main__':
    thread1 = threading.Thread(
        group=None,
        target=(process_order),
        name='Order_proceeser_1',
        args=(123,),
        kwargs={'priority' : 4}
    )

    # print(threading.current_thread().name) # Main_thread
    # print(thread1.ident) #None
    # thread1.start()
    # print(thread1.ident)

    print(thread1.is_alive())
    thread1.start()
    print(thread1.is_alive())
    thread1.join()
    print(thread1.is_alive())

