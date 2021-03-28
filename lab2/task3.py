"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

from threading import Thread, Semaphore, Lock
import random

NO_THREADS = 10


class Coffee:
    """ Base class """
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        """ Returns the coffee name """
        return self.name

    def get_size(self):
        """ Returns the coffee size """
        return self.size

    def get_message(self):
        pass


class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self, "espresso", size)
        self.size = size

    def get_message(self):
        """ Output message """
        return "nice {} {}".format(self.get_size(), self.get_name())


class Cappuccino(Coffee):
    def __init__(self, size):
        Coffee.__init__(self, "cappuccino", size)
        self.size = size

    def get_message(self):
        """ Output message """
        return "italian {} {}".format(self.get_size(), self.get_name())


class Americano(Coffee):
    def __init__(self, size):
        Coffee.__init__(self, "americano", size)
        self.size = size

    def get_message(self):
        """ Output message """
        return "strong {} {}".format(self.get_size(), self.get_name())


class Distributor():
    def __init__(self):
        self.full = Semaphore(value=0)
        self.empty = Semaphore(value=NO_THREADS)
        self.prod_mutex = Lock()
        self.cons_mutex = Lock()
        self.size = 100
        self.buffer = []
        self.current_pos = 0

    def get_prod(self):
        return self.prod_mutex

    def get_cons(self):
        return self.cons_mutex

    def get_full(self):
        return self.full

    def get_empty(self):
        return self.empty

    def put_coffee(self, coffee):
        self.empty.acquire()
        self.prod_mutex.acquire()
        self.buffer.append(coffee)
        self.current_pos = (self.current_pos + 1) % self.size
        self.prod_mutex.release()
        self.full.release()

    def take_coffee(self):
        self.full.acquire()
        self.cons_mutex.acquire()
        coffee = self.buffer[self.current_pos - 1]
        if (self.current_pos > 0):
            self.current_pos -= 1
        self.cons_mutex.release()
        self.empty.release()
        return coffee


class CoffeeFactory(Thread):
    def __init__(self, id, dis):
        Thread.__init__(self)
        self.id = id
        self.dis = dis
        self.coffees = ["americano", "espresso", "cappuccino"]
        self.sizes = ["small", "medium", "large"]

    def run(self):
        while True:
            size = random.choice(self.sizes)
            type = random.choice(self.coffees)
            if type == "americano":
                coffee = Americano(size)
            elif type == "espresso":
                coffee = Espresso(size)
            elif type == "cappuccino":
                coffee = Cappuccino(size)

            self.dis.put_coffee(coffee)
            print("Factory {} {}".format(self.id, coffee.get_message()))


class User(Thread):
    def __init__(self, id, dis):
        Thread.__init__(self)
        self.id = id
        self.dis = dis

    def run(self):
        while True:
            coffee = self.dis.take_coffee()
            print("Consumer {} {}".format(self.id, coffee.get_name()))


def main():
    producers = []
    consumers = []
    dis = Distributor()
    for i in range(NO_THREADS):
        producers.append(CoffeeFactory(i, dis))
        consumers.append(User(i, dis))

    for t in producers:
        t.start()

    for t in consumers:
        t.start()

    for i in producers:
        i.join()

    for i in consumers:
        i.join()


if __name__ == '__main__':
    main()
