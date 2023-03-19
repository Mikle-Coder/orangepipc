import threading
import time
import queue

class Timer:
    def __init__(self):
        self._thread = None
        self._is_running = False
        self._start_time = None
        self._elapsed_time = None
        self._seconds_elapsed = None
        self.callback= None

    def start(self):
        self._is_running = True
        self._start_time = time.monotonic()
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def stop(self):
        self._is_running = False
        self._thread.join()

    def add_callback(self, callback):
        self.callback = callback

    def _run(self):
        current_time = time.monotonic()
        self._elapsed_time = current_time - self._start_time
        self._seconds_elapsed = self._elapsed_time
        while self._is_running:
            current_time = time.monotonic()
            self._elapsed_time = current_time - self._start_time
            if(int(self._seconds_elapsed) < int(self._elapsed_time)):
                self.callback()
            self._seconds_elapsed = self._elapsed_time

            time_since_last_second = self._elapsed_time % 1

            if time_since_last_second < 0.01:
                time.sleep(0.01 - time_since_last_second)

def show():
    print(1)

timer = Timer()
timer.add_callback(show)
timer.start()