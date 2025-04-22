class calculator:
    """
    Классический калькурлятор с добавлением метода: 
    convert_precision - вычисление количества чисел после запятой по заданному tolerance
    """    
    def __init__(self, tolerance:float = 10**-6):
        self.tolerance = tolerance

    def convert_precision(self):
        counter = 0
        step = self.tolerance
        while (step - int(step) != 0):
            counter += 1
            step *= 10
        return counter

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            precision = self.convert_precision()
            return round(x1/x2, precision)


