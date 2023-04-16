import sys


class Recipe:
    def __init__(self, name=None, cook_lv=None, cook_time=None,
                 ingr=None, descrip="", recipe_type=None):
        if None in locals().values():
            print("Null argument not expected")
            exit()
        try:
            self.name = str(name)  # This calls ValueError
            self.cooking_lvl = int(cook_lv)
            self.cooking_time = int(cook_time)
            self.ingredients = list(ingr)
            self.description = str(descrip)
            self.recipe_type = str(recipe_type)

            if len(name) == 0:
                raise Exception("Recipe's name empty")  # This calls Exception
            if cook_lv > 5 or cook_lv < 1:
                raise Exception("Cooking level is not between 1 and 5")
            if cook_time < 0:
                raise Exception("Moron! Time is not negative...")
            if len(ingr) == 0:
                raise Exception("How will you cook with no ingredients?")
            if recipe_type not in ['lunch', 'starter', 'dessert']:
                raise Exception("Recipe type not correct, choose 'starter','lunch' or 'dessert'")
        except (Exception, ValueError) as e:
            print("Recipe exception raised:", repr(e))
            sys.exit(0)
    def __str__(self):
        '''
        Return the string to print with the recipe info
        '''
        txt = "NAME: " + self.name + ", COOKING LEVEL: " + str(self.cooking_lvl) + ", COOKING TIME: " + str(self.cooking_time) + ", INGREDIENTS: "
        for ing in self.ingredients:
            txt += ing + ", "
        txt += "DESCRIPTION: " + self.description + ", RECIPE TYPE: " + self.recipe_type
        return txt


if __name__ == "__main__":
    tourte = Recipe("Galletas", 2, 20, ["Harina", "levadura", "huevos"], "", "lunch")
    to_print = str(tourte)
    print(to_print)
