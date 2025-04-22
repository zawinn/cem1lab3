import math

class Calculator:   
    
    # Создаем конструктор класса
    def __init__(self, tolerance:float = 10**-6):
        self.tolerance = tolerance
    
    # К
    def convert_precision(self):
        counter = 0
        step = self.tolerance
        while (step - int(step) != 0):
            counter += 1
            step *= 10
        return counter

    def add(self, *args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def multiply(self, *args):
        sum = 1
        for i in args:
            sum *= i
        return sum

    def subtract(self, x1, x2):
        return x1-x2
    
    def divide(self, x1, x2):
        if x2 != 0:
            precision = self.convert_precision()
            return round(x1/x2, precision)

    def medium(self, *args):
        sum = 0
        precision = self.convert_precision()
        for i in args:
            sum += i
        return round(sum/len(args), precision)
    
    def variance(self, *args):
        medium = self.medium(*args)
        precision = self.convert_precision()
        temporary = 0
        for i in args:
            temporary += (i - medium)**2
        return round(temporary/len(args), precision)
    
    def std_deviation(self, *args):
        precision = self.convert_precision()
        return round(math.sqrt(self.variance(self, *args)), precision)
    
    def median(self, *args):
        numbers = []
        precision = self.convert_precision()
        flag = True
        for i in args:
            if isinstance(i, list):
                numbers = i
                flag = False
                break
        if flag:        
            numbers = [*args]
        numbers.sort()
        if (len(numbers) % 2 == 1):
            return numbers[(len(numbers)//2)]
        else:
           return round((numbers[(len(numbers)//2)] + numbers[(len(numbers)//2) - 1]) / 2, precision)
    
    def median_extension(self, *args):
        list = [*args]
        list.sort()
        precision = self.convert_precision()
        first_half_of_list = [list[i] for i in range(len(list)//2)] 
        second_half_of_list = [list[i] for i in range(len(list)//2 if len(list) % 2 == 0 else len(list)//2 + 1, len(list))] 
        return round(self.median(second_half_of_list) - self.median(first_half_of_list), precision)
      
a = Calculator(0.001).median_extension(1, 2, 3, 4)
print(a)