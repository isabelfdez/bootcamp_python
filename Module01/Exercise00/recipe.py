class Recipe:
    def __init__(self, name = None, cook_lv = None, cook_time = None,
                    ingr = None, descrip = None, recipe_type = None):
        if None in locals().values():
            print("Null argument not expected")
            exit()
        try:
            self.name = str(name)
            self.cooking_lvl = int(cook_lv)
            self.cooking_time = int(cook_time)
            self.ingredients = list(ingr)
            self.description = str(descrip)
            self.recipe_type = str(recipe_type)

            if len(name) == 0:
                raise Exception("Recipe's name empty")
            if cook_lv > 5 or cook_lv < 1:
                raise Exception("Cooking level is not between 1 and 5")
            if cook_time < 0:
                raise Exception("Moron ! Time is not negative...")
            if len(ingr) == 0:
                raise Exception("No ingredients required?")
            if recipe_type not in ['lunch', 'starter', 'dessert']:
                raise Exception("Recipe type not correct, choose 'starter' or 'lunch' or 'dessert'")
        except (Exception, ValueError) as e:
            print("Recipy exception raised:", repr(e))
            exit()