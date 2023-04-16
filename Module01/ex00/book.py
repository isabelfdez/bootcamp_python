import datetime
from recipe import Recipe


class Book:
    def __init__(self, name="Default name"):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        '''
        Prints a recipe with the name \texttt{name} and returns the instance
        '''
        for recipes in self.recipes_list.values():
            for meal in recipes:
                if (meal.name == name):
                    print(str(meal))
                    return (meal)
        print("Recipe does not exist")
        return None

    def get_recipes_by_types(self, recipe_type):
        '''
        Get all recipe names for a given recipe_type
        '''
        type = self.recipes_list.get(recipe_type)
        if (type is None):
            print("Recipe type does not exist")
            return []
        recipe_names = [meal.name for meal in self.recipes_list[recipe_type]]
        return (recipe_names)

    def add_recipe(self, recipe):
        '''
        Add a recipe to the book and update last_update
        '''
        if (not isinstance(recipe, Recipe)):
            print("Given argument is not a recipe")
            return
        type = recipe.recipe_type
        for recipes in self.recipes_list.values():
            for meal in recipes:
                if (meal.name == recipe.name):
                    print(f"You already have a {type} named {recipe.name}")
                    return
        self.recipes_list[type].append(recipe)
        self.last_update = datetime.datetime.now()
