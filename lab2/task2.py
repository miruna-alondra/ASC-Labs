"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
import sys
from random import randint
from threading import Thread, current_thread


class MyThread(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self.number = number

    def run(self):
        print("Hello, I'm Thread", current_thread().name, "and I received the number ", self.number)

threads = []
num_threads = int(sys.argv[1])
for i in range(num_threads):
    threads.append(MyThread(randint(0, 10000)))

for t in threads:
    t.start()

for i in threads:
    i.join()
