

def calc_shape(listy: list) -> tuple:
    """This function receives the values and returns the shape of the vector"""
    a = len(listy)
    b = len(listy[0])
    ret = (a, b)
    return ret

def get_value(vector, index: int) -> float or int:
    """This function returns the index-th element of the vector passed as first argument"""
    if (vector.shape[0] == 1 and index < vector.shape[1]): # Row vector
        return vector.values[0][index]
    if (vector.shape[1] == 1 and index < vector.shape[0]): # Column vector
        return vector.values[index][0]
    else:
        raise ValueError("Index out of bound")

class Vector:
    def __init__(self, arg):
        if (isinstance(arg, (list, int, tuple)) is False):
            raise ValueError("Incorrect initialization")
        if (isinstance(arg, int)):
            if (arg < 0):
                raise ValueError("Size cannot be negative")
            else:
                self.values = [[float(i)] for i in range(0, arg)]
                self.shape = (arg, 1)
        # Do this exceptions have to exit?
        elif isinstance(arg, tuple):
            if ((len(arg) != 2) or
               not all([isinstance(obj, int) for obj in arg]) or
               (arg[0] >= arg[1])):
                raise ValueError("Tuple format is wrong")
            else:
                self.values = [[float(i) for i in range(arg[0], arg[1])]]
                self.shape = (arg[1] - arg[0], 1)
        elif isinstance(arg, list):
            for elem in arg:
                if (isinstance(elem, list) is False):
                    raise ValueError("Incorrect initialization")
                if (not all([isinstance(nb, float) for nb in elem])):
                    raise ValueError("Incorrect initialization")
            self.values = arg
            self.shape = calc_shape(arg)
    
    def dot(self, vector) -> float or int:
        """Calculates the dot product of two vectors"""
        if (isinstance(vector, Vector) is False):
            raise ValueError("Argument is not a vector")
        elif (self.shape != vector.shape[::-1]):
            raise ValueError("Shapes are incompatible. Dot product cannot be calculated")
        res = 0
        rang = max(self.shape[0], self.shape[1])
        for i in range(rang):
            res += get_value(self, i) * get_value(vector, i)
        return res
    
    def T(self):
        """Calculates the transpose of the given vector"""
        if (self.shape[0] == 1):  # Row vector
            transpose = [[x] for x in self.values[0]]
        else:  # Column vector
            transpose = [[x[0] for x in self.values]]
        return Vector(transpose)

    # MAGIC METODS
    def __add__(self, vector):
        if (isinstance(vector, Vector) is False):
            raise ValueError("Argument is not a vector")
        elif (self.shape != vector.shape):
            raise ValueError("Shapes are incompatible. Dot product cannot be calculated")
        else:
            rang = max(self.shape[0], self.shape[1])
            values = [get_value(self, i) + get_value(vector, i) for i in range(rang)]
            return (Vector([values]) if self.shape[0] == 1 else Vector([values]).T())

