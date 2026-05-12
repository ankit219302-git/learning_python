# A threads actual target function can be wrapped inside another function (called wrapper function) acting as target.
# Wrapper functions in Python threading are primarily used to encapsulate a target function,
# allowing us to modify, enhance, or manage its behavior when it runs in a separate thread without altering the original code.
# They are highly useful for injecting functionality like
# logging, error handling, performance timing, or locking (thread safety) before or after the target task runs.
import time
from threading import Thread

from src.multithreading.globalinterpreterlock import increment


def timed_task(thread_name, func_name):
    # time.perf_counter() is better for benchmarking than time.time().
    # The primary difference is that time.time() measures absolute "wall-clock" time (what time it is),
    # while time.perf_counter() is a high-resolution (more precise) timer
    # designed specifically for measuring durations (how long something took).
    #
    # Key Differences -
    # - Monotonicity: time.time() is subject to system clock adjustments,
    #                 such as NTP synchronization or manual updates.
    #                 This means if the clock is set back while our code is running,
    #                 the calculated duration could be negative.
    #                 time.perf_counter() is monotonic, meaning it never moves backward,
    #                 making it reliable for measuring elapsed time.
    # - Precision: Per the Python documentation, perf_counter() provides the highest available resolution
    #              on a specific hardware, making it far superior for timing small code segments.
    # - Reference Point: time.time() returns a specific date-time value (seconds since 1970).
    #                    In contrast, the absolute value returned by perf_counter() is meaningless on its own;
    #                    it is only useful when we subtract a start time from an end time to find a difference.
    #
    # Which one to use?
    #   Use time.perf_counter() if trying to see how fast a function runs or benchmarking performance.
    #   Use time.time() if we need to record a timestamp for a log or know the actual calendar date and time.
    start_time = time.perf_counter()
    func_name()         # increment() function called here
    print(f"Time taken by {thread_name}: {time.perf_counter() - start_time} seconds")

if __name__ == '__main__':
    thread = Thread(target=timed_task, args=("Test_Worker_Thread", increment))
    thread.start()
