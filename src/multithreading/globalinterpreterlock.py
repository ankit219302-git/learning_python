import time
from threading import Thread

# The Global Interpreter Lock (GIL) is one of the most famous (and controversial) parts of CPython.
# It explains why Python threading behaves differently from languages like Java, Go, or C++.
#
# The GIL is a global lock inside the CPython interpreter that allows
# only ONE thread to execute Python bytecode at a time,
# even on a multicore CPU.

COUNT = 50_000_000

def increment():
    x = 0
    for _ in range(COUNT):
        x += 1

def decrement():
    x = COUNT
    for _ in range(COUNT):
        x -= 1

def calculate_time_taken(start_time, env_type):
    print(f"Total time taken in {env_type} run: {(time.perf_counter() - start_time):.10f} seconds")

if __name__ == '__main__':
    thread1 = Thread(target=increment)
    thread2 = Thread(target=decrement)

    # time.perf_counter() is better for benchmarking than time.time().
    # The primary difference is that time.time() measures absolute "wall-clock" time (what time it is),
    # while time.perf_counter() is a high-resolution (more precise) timer
    # designed specifically for measuring durations (how long something took).
    # More details in wrapperfunctions.py
    multithreaded_start_time = time.perf_counter()
    thread1.start()
    thread2.start()
    # Here we need the threads to finish execution before proceeding, hence .join() usage.
    # When we call .join(), the main program pauses and waits at that specific line (thread1.join())
    # until thread1 completely finishes its increment task.
    # Here is how the execution flow works:
    #   1. thread1.start() and thread2.start(): Both threads begin running in the background immediately.
    #   2. thread1.join(): The main thread stops here. Even if thread2 finishes first,
    #                      the program won't move past this line until thread1 is done.
    #   3. thread2.join(): Once thread1 finishes, the program moves to this line.
    #                      If thread2 is already done, it moves on instantly; if not, it waits again.
    #
    # Nonetheless, even on using .join(), the thread runs will switch between thread1 and thread2,
    # no matter which thread's join() is holding the program main thread execution currently.
    thread1.join()
    thread2.join()

    # This can be used to detect when the program ends
    # and run the calculate_time_taken() function right before exiting the program
    # without holding the main thread using join().
    # atexit.register(calculate_time_taken, multithreaded_start_time, "multi-threaded")

    print()
    calculate_time_taken(multithreaded_start_time, env_type="multithreaded")

    # If Python was truly running the threads parallely,
    # the below code would have taken approximately twice as much time as the multithreaded one.
    # But, that is not the case.
    #
    # SAMPLE OUTPUT -->
    # Total time taken in multithreaded run: 2.5519981384 seconds
    # Total time taken in sequential run: 2.5427258015 seconds
    sequential_start_time = time.perf_counter()
    increment()
    decrement()
    calculate_time_taken(sequential_start_time, env_type="sequential")
