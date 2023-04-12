cookbook = {'Sandwich' : {'ingredients' : ['ham', 'bread', 'cheese'],
                        'meal' : 'lunch', 'prep_time': 10},
            'Cake' : {'ingredients' : ['flour', 'sugar', 'eggs'],
                        'meal' : 'dessert', 'prep_time': 60},
            'Salad' : {'ingredients' : ['avocado', 'argula', 'tomatoes', 'spinach'],
                        'meal' : 'lunch', 'prep_time': 15}}

def print_recipes_names():
    print(cookbook.keys())

def print_recipe_details(recipe):
    print("Recipe for " + recipe + ": ")
    print("Ingredients list: ", cookbook[recipe]['ingredients'])
    print("To be eaten for " + cookbook[recipe]['meal'] + ".")
    print("Takes " + str(cookbook[recipe]['prep_time']) + " minutes of cooking.")

def delete_recipe(recipe):
    del cookbook[recipe]

def add_recipe():
    name = input("Enter a name: ")
    print("Enter ingredients: ", end = "")
    ingredients = []
    while True:
        line = input()
        if (line == ""):
            break
        ingredients.append(line)
    type = input("Enter a meal type: ")
    time = input("Enter a preparation time: ")
    value = {'ingredients' : ingredients, 'meal' : type, 'prep_time': int(time)}
    cookbook[name] = value

print("Welcome to the Python Cookbook !")
print("List of available options:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")

while True:
    option = input("Please select an option: ")
    try:
        int_option = int(option)
    except:
        print("Sorry, this option does not exist.")
        print("List of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        continue
    if (int_option < 1 or int_option > 5):
        print("Sorry, this option does not exist.")
        print("List of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
    if (int_option == 1):
        add_recipe()
    elif (int_option == 2):
        recipe = input("Please enter a recipe name to delete it: ")
        delete_recipe(recipe)
    elif (int_option == 3):
        recipe = input("Please enter a recipe name to get its details: ")
        print_recipe_details(recipe)
    elif (int_option == 4):
        for recipe in cookbook.keys():
            print_recipe_details(recipe)
    elif (int_option == 5):
        print("Cookbook closed. Goodbye !")
        quit()

