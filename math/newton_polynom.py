# Netwon Polynome

### General Formula for getting function value fi(x)
# fi(x) = a0 + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1)) + ... + (ai * (x-x0)*...*(x - x-1))

### General formula for getting alpha value (an) an, based on all points until pn and last alphas
# an = [fn(x) - [a0  + (a1 * (x-x0)) + (a2 * (x-x0)(x-x1)) + ... + (an-1 * (x-x0)(x-x1)*...*(x-xn-2))] / (x-x0)(x-x1)*...(x-x-1) 

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
    def __init__(self, alphaIndex, alphaValue, point) -> None:
        self.index = alphaIndex
        self.value = alphaValue
        self.point = point
    
    def __str__(self) -> str:
        return f"Alpha{self.index} for Point {self.point}: {self.value}"

points = [
    Point(1,2),
    Point(2,-2),
    Point(3,4)
]

# discover alphas
alphas = []
for indexA, point in enumerate(points):
    
    fnx = point.y

    sum = 0
    for alphaIndex, alpha in enumerate(alphas):
        unknownX = 1
        for xIndex in range(alphaIndex):
            if unknownX == 0:
                break
            unknownX *= point.x - points[xIndex].x

        multiplication = alpha * unknownX
        sum += multiplication
    numerator = fnx - sum

    denominator = 1
    for index in range(indexA - 1):
        if denominator == 0:
            break
        denominator *= point.x - points[index].x
    
    alpha = numerator / denominator
    alphas.append(alpha)

class Logger():
    def __init__(self):
        self.messageX = ""
        self.messageComplete = ""
        self.result = ""
    
    def new_alpha_function(self, x):
        self.__init__()
        self.points = points
        self.index_greathest_alpha = len(points) -1

        self.messageX += f"f{self.index_greathest_alpha}(x) = "
        self.messageComplete += f"f{self.index_greathest_alpha}({x}) = "
    
    def add_alpha(self, index, value):
        self.messageX += f"(a{index}"
        self.messageComplete += f"({value}"

    def add_new_partial_coeficient_for_alpha(self, x, xIndex, index):
        self.messageX += f" * (x-x{index})"
        self.messageComplete += f" * ({x-xIndex})"

    def close_alpha(self):
        self.messageX += f")"
        self.messageComplete += f")"
    
    def add_result(self, result):
        self.result += f"Result: {result}"
    
    def get_start_message(self):

        start_message = f"Calculating the value of f{self.index_greathest_alpha}(x) using polynomial interpolation: \n\n"
        start_message += f"Points used:\n"
        for index, point in enumerate(self.points):
            start_message += f"Point {index}: {point} | a{index} = {alphas[index]} \n"


        return start_message
    
    def print(self):
        print()
        print(self.get_start_message())
        print(self.messageX)
        print(self.messageComplete)
        print()
        print(f"-----> {self.result}")
        print()
        print()
        print("-----------------------------------------")


def calculate(x, logger=Logger()):
    result = 0
    
    logger.new_alpha_function(x)

    for index, alpha in enumerate(alphas):
        logger.add_alpha(index, alpha)
        coefizient = 1
        for indexA in range(index):
            xIndex = points[indexA].x
            coefizient *= x-xIndex
            logger.add_new_partial_coeficient_for_alpha(x, xIndex, indexA)
        lastFunctionValue = alpha * coefizient
        logger.close_alpha()

        result += lastFunctionValue
    
    logger.add_result(result)

    logger.print()
    return result




calculate(1)
calculate(2)
calculate(3)
calculate(10)


