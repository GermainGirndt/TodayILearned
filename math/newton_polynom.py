# Netwon Polynome

### General Formula for getting function value fi(x)
# fi(x) = a0 + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1)) + ... + (ai * (x-x0)*...*(x - x-1))

### General formula for getting alpha value (an), based on all points until pn and last alphas
# an = {fn(x) - [a0  + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1)) + ... + (an-1 * (x-x0)(x-x1)*...*(x-xn-2))]} / (x-x0)(x-x1)*...(x-x-1) 

### Intuition
# # at first, we must discover the values of alphas to recreate the formula

### Example - Points (1, 2), (2, -2) and (3, 4)

# Discovering Alpha0 through Point(1, 2)
# f0(x) = a0
# f0(1) = a0
# 2 = a0

# Discovering Alpha0 through Point(2, -2) + last alphas and points
# f1(x) = a0 + (a1 * (x-x0))
# f1(x) = a0 + (a1 * (x-x0))
# f1(2) = a0 + (a1 * (2-1))
# -2 = a0 + (a1 * (2-1))
# -2 = 2 + (a1 * 1)
# -4 = a1

# Discovering Alpha0 through Point(3, 4) + last alphas and points
# f2(x) = a0 + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1))
# f2(3) = a0 + (a1 * (3-x0)) + (a2 * (3-x0)(3-x1))
# 4 = a0 + (a1 * (3-x0)) + (a2 * (3-x0)(3-x1))
# 4 = a0 + (a1 * (3-1)) + (a2 * (3-1)(3-2))
# 4 = 2 + (-4 * (3-1)) + (a2 * (3-1)(3-2))
# 4 = 2 + (-4 * 2) + (a2 * (2) * 1)
# 4 = 2  - 8 + 2*a2
# 10 = 2a2
# 5 = a2

# Formula using alphas and points calculated so far: 
# f2(x) = 2 + (-4 * (x-1)) + (a2 * (x-1)(x-2))
# note: in the algorithm bellow the x coeficients can be memoized for posterior access
# but I opted for not doing that, since I wanted to keep in track of every step

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"


class Alpha:
    def __init__(self, alpha_index, alpha_value, point) -> None:
        self.index = alpha_index
        self.value = alpha_value
        self.point = point
    
    def __str__(self) -> str:
        return f"Alpha{self.index} for Point {self.point}: {self.value}"


### Logger

class Logger():
    def __init__(self, points):
        self.formula_message = ""
        self.complete_message = ""
        self.result = ""
        self.alphas = []
        self.points = points
    
    def clean(self):
        self.formula_message = ""
        self.complete_message = ""
        self.result = ""
        #self.add_alphas = []
    
    def add_alphas(self, alphas):
        self.alphas = alphas
    
    def new_alpha_function(self, x):
        self.clean()
        self.index_greathest_alpha = len(points) -1

        self.formula_message += f"f{self.index_greathest_alpha}(x) = "
        self.complete_message += f"f{self.index_greathest_alpha}({x}) = "
    
    def add_alpha(self, index, value):
        self.formula_message += f"(a{index}"
        self.complete_message += f"({value}"

    def add_new_partial_coeficient_for_alpha(self, x, x_index, index):
        self.formula_message += f" * (x-x{index})"
        self.complete_message += f" * ({x-x_index})"

    def close_alpha(self):
        self.formula_message += f")"
        self.complete_message += f")"
    
    def add_result(self, result):
        self.result += f"Result: {result}"
    
    def get_start_message(self):
        start_message = f"Calculating the value of f{self.index_greathest_alpha}(x) using polynomial interpolation: \n\n"

        return start_message

    def get_and_alphas_points_used(self):
        message = f"\n + + +\n"
        message += f"\nPoints and Alphas used:\n\n"
        for index, point in enumerate(self.points):
            message += f"Point {index}: {point} -> a{index} = {self.alphas[index]} \n"
        message += f"\n + + +\n\n"
        return message
    
    def print_points_and_alphas_used(self):
        print(self.get_and_alphas_points_used())

    def print(self):
        print()
        print(self.get_start_message())
        print(self.formula_message)
        print(self.complete_message)
        print()
        print(f"-----> {self.result}")
        print()
        print()
        print("-----------------------------------------")

class Newton:
    def __init__(self, points, logger):
        self.points = points
        self.logger = logger
        self.alphas = []
    
    ### General formula for getting alpha value (an), based on all points until pn and last alphas
    # an = {fn(x) - [a0  + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1)) + ... + (an-1 * (x-x0)(x-x1)*...*(x-xn-2))]} / (x-x0)(x-x1)*...(x-x-1) 

    def discover_alphas(self):

        for index_a, point in enumerate(self.points):
            formula_message = f""
            calc_message = f""
            sub_result_message = f""
            result_message = f""
    
            fnx = point.y
            sum = 0
            formula_message += f"a{index_a} =" + " { " + f"f{index_a}({point.x})"
            calc_message += f"a{index_a} =" + " { " + f"{point.y}"

            if len(self.alphas) != 0:
                formula_message += f" - ["
                calc_message += f" - ["

            for alpha_index, alpha in enumerate(self.alphas):

                if alpha_index == 0:
                    formula_message += f"(a{alpha_index}"
                    calc_message += f"({alpha}"
                else:
                    formula_message += f" + (a{alpha_index}"
                    calc_message += f" + ({alpha}"
                unknownX = 1
                for x_index in range(alpha_index):
                    if unknownX == 0:
                        break
                    unknownX *= point.x - points[x_index].x
                    formula_message += f" * (x - x{x_index})"
                    calc_message += f" * ({point.x} - {points[x_index].x})"
                formula_message += f")"
                calc_message += f")"

                multiplication = alpha * unknownX
                sum += multiplication


            numerator = fnx - sum
            if len(self.alphas) != 0:
                formula_message += f"]"
                calc_message += f"]"

            formula_message += " } / "
            calc_message += " } / "            
            if index_a == 0:
                formula_message += "1"
                calc_message += "1"

            denominator = 1
            print(index_a)
            for index in range(index_a): # -1?
                print("aaaaa")
                if denominator == 0:
                    break
                denominator *= point.x - points[index].x
                print(point.x)
                print(points[index].x)
                print(point.x - points[index].x)
                print("abbbbbba")
                if index == 0:
                    formula_message += f"(x - x{index})"
                    calc_message += f"({point.x} - {points[index].x})"
                else:                    
                    formula_message += f" * (x - x{index})"
                    calc_message += f" * ({point.x} - {points[index].x})"
            
            print(numerator)
            print(denominator)
            
            alpha = numerator / denominator
            self.alphas.append(alpha)
            print()
            print(formula_message)
            print(calc_message)
            print()
            print(f"a{index_a} = {alpha}")
            print("+++")
            print()
        self.logger.add_alphas(self.alphas)
    
    def calculate(self, x):
        result = 0
        
        self.logger.new_alpha_function(x)

        for index, alpha in enumerate(self.alphas):
            self.logger.add_alpha(index, alpha)
            coefizient = 1
            for index_a in range(index):
                x_index = points[index_a].x
                coefizient *= x-x_index
                self.logger.add_new_partial_coeficient_for_alpha(x, x_index, index_a)
            last_function_value = alpha * coefizient
            self.logger.close_alpha()

            result += last_function_value
        
        self.logger.add_result(result)
        return result

# Here you can add the points, which the polynom has to run into:
points = [
    Point(1,2),
    Point(2,-2),
    Point(3,4)
]

logger = Logger(points)
newton = Newton(points, logger)


# Here you get the function values (y) for any x using the calculated polynom
numbers_to_calculate = [1, 2, 3]

newton.discover_alphas()
logger.print_points_and_alphas_used()
for number in numbers_to_calculate:
    newton.calculate(number)
    logger.print()

