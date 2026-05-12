from threading import Thread

from src.loop.for_range import increment_and_print, decrement_and_print

if __name__ == '__main__':
    # A Python thread is just a regular OS thread.
    # When we execute any program there's always a MainThread that is created for execution.
    # Any additional thread (worker thread) we create is in addition to this one.
    #
    # One thing to remember when writing multithreading programs in Python,
    # is that they only have limited use due to the infamous Global Interpreter Lock (GIL).
    # In short, using threads won't make CPU-intensive program any faster, even on a multicore machine.
    # The GIL exists to prevent race conditions in Python's internal memory management,
    # particularly its reference-counting system.
    #
    # Even MainThread is run concurrently (switching) rather than parallely (true parallelism) with other threads,
    # i.e., the MainThread as well has to wait for the GIL lock (if acquired by any worker thread) for resuming its execution.
    #
    # However, when threads wait for:
    # - network
    # - disk
    # - database
    # - sleep
    # Python releases the GIL.
    # Thus, they can be useful when performing something involving waiting.
    # Like, for I/O-bound tasks where while one thread is waiting for a network response or reading a file,
    # the OS can switch to another thread to continue working.
    #
    # CPython, however, periodically switches threads.
    # Older versions: every N bytecode instructions
    # Modern versions: time-based switching (called "time-slicing"), usually every few milliseconds,
    #                  creating the illusion of simultaneous activity.
    thread1 = Thread(target=increment_and_print, args=[151])
    thread2 = Thread(target=decrement_and_print, args=[200])

    thread1.start()
    thread2.start()

    # Unless the thread is a "daemon thread" (enabled via setting the constructor argument 'daemon' or the 'daemon' property to True),
    # it will be implicitly joined for before the program exits, otherwise, it is killed abruptly.
    # That is why, thread.join() is not necessarily needed here
    # as the Python program will wait for these threads to finish before exiting, even if we never call .join()
    thread1.join()
    thread2.join()
