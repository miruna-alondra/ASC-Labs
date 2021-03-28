"""
A command-line controlled coffee maker.
"""

import sys
import load_recipes as rec

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

#print("I'm a simple coffee maker")
#print("Press enter")
#sys.stdin.readline()
#print("Teach me how to make coffee...please...")
def status():
    print("water: " + RESOURCES[WATER].__str__() + "%")
    print("coffee: " + RESOURCES[COFFEE].__str__() + "%")
    print("milk: " + RESOURCES[MILK].__str__() + "%")

def refill():
    print("Which resource?")
    resource = sys.stdin.readline().strip()
    if resource == WATER:
        RESOURCES[WATER] = 100
    elif resource == COFFEE:
        RESOURCES[COFFEE] = 100
    elif resource == MILK:
        RESOURCES[MILK] = 100
    elif resource == "all":
        RESOURCES[WATER] = 100
        RESOURCES[COFFEE] = 100
        RESOURCES[MILK] = 100
    print("water: " + RESOURCES[WATER].__str__() + "%")
    print("coffee: " + RESOURCES[COFFEE].__str__() + "%")
    print("milk: " + RESOURCES[MILK].__str__() + "%")

def make_coffee():
    print("Which coffee?")
    coffee_type = sys.stdin.readline().strip()
    recipe = rec.get_recipes(coffee_type)
    if coffee_type == "cappuccino":
        if RESOURCES[WATER] >= 5:
            RESOURCES[WATER] = RESOURCES[WATER] - int(recipe[0])
        if RESOURCES[COFFEE] >= 10:
            RESOURCES[COFFEE] = RESOURCES[COFFEE] - int(recipe[1])
        if RESOURCES[MILK] >= 10:
            RESOURCES[MILK] = RESOURCES[MILK] - int(recipe[2])
    elif coffee_type == "espresso":
        if RESOURCES[WATER] >= 5:
            RESOURCES[WATER] = RESOURCES[WATER] - int(recipe[0])
        if RESOURCES[COFFEE] >= 10:
            RESOURCES[COFFEE] = RESOURCES[COFFEE] - int(recipe[1])
        RESOURCES[MILK] = RESOURCES[MILK] - int(recipe[2])
    elif coffee_type == "americano":
        if RESOURCES[WATER] >= 10:
            RESOURCES[WATER] = RESOURCES[WATER] - int(recipe[0])
        if RESOURCES[COFFEE] >= 10:
            RESOURCES[COFFEE] = RESOURCES[COFFEE] - int(recipe[1])
        RESOURCES[MILK] = RESOURCES[MILK] - int(recipe[2])
    print("Here is your {}!:)".format(coffee_type))

def list():
    print("americano, {}, {}".format("cappuccino", "espresso"))

def main():
    print("Enter command")

    while 1:
        read_input = sys.stdin.readline().strip()
        if read_input == EXIT:
            print("Have a nice day!:3")
            break
        elif read_input == RESOURCE_STATUS:
            status()
        elif read_input == REFILL:
           refill()
        elif read_input == LIST_COFFEES:
            list()
        elif read_input == HELP:
            list()
        elif read_input == MAKE_COFFEE:
            make_coffee()



if __name__ == "__main__":
    main()
