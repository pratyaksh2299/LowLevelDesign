import threading
import time

def background_cleanup():
    while True:
        print("Cleaning up cache...")
        time.sleep(5)

# Daemon thread - won't prevent program exit
daemon = threading.Thread(target=background_cleanup, daemon=True)
daemon.start()

# Alternatively, set daemon after creation
thread = threading.Thread(target=background_cleanup)
thread.daemon = True  # Must set before start()
thread.start()