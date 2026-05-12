from threading import Thread

from src.loop.for_range import increment_and_print, decrement_and_print

if __name__ == '__main__':
    # Daemon threads are background threads that are
    # abruptly killed when all non-daemon threads (usually just the main thread) finish.
    # They do not keep the process alive.
    # Hence we need .join() to keep them alive by making the main thread wait for these threads to finish before exiting.

    thread1 = Thread(target=increment_and_print, args=[201], daemon=True)
    # Or the daemon thread could have been created like this -
    # thread1 = Thread(target=increment_and_print, args=[201])
    # thread1.daemon = True
    thread2 = Thread(target=decrement_and_print, args=[150])

    thread1.start()
    thread2.start()

    # We need thread1.join() here to keep it alive else the increment_and_print() function might exit before completion.
    # thread2.join() is not needed since it's a non-daemon thread.
    thread1.join()
