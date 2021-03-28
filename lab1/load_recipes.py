"""
	Bonus task: load all the available coffee recipes from the folder 'recipes/'
	File format:
		first line: coffee name
		next lines: resource=percentage

	info and examples for handling files:
		http://cs.curs.pub.ro/wiki/asc/asc:lab1:index#operatii_cu_fisiere
		https://docs.python.org/3/library/io.html
		https://docs.python.org/3/library/os.path.html
"""

RECIPES_FOLDER = "recipes"
def get_recipes(coffee_type):
    if coffee_type == "americano":
        f = open("americano.txt", "r")
        #print(f.readline())
        f.readline()
        #print(f.readline().split("=")[1].strip())
        water = f.readline().split("=")[1].strip()
        coffee = f.readline().split("=")[1].strip()
        milk = f.readline().split("=")[1].strip()
        list = [water, coffee, milk]
        return list
    elif coffee_type == "espresso":
        f = open("espresso.txt", "r")
        f.readline()
        water = f.readline().split("=")[1].strip()
        coffee = f.readline().split("=")[1].strip()
        milk = f.readline().split("=")[1].strip()
        list = [water, coffee, milk]
        return list
    elif coffee_type == "cappuccino":
        f = open("cappuccino.txt", "r")
        f.readline()
        water = f.readline().split("=")[1].strip()
        coffee = f.readline().split("=")[1].strip()
        milk = f.readline().split("=")[1].strip()
        list = [water, coffee, milk]
        return list
        #f.close()