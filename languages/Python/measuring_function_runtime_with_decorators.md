## Measunring function runtime with decorators


```
import time
import functools


def timer(func):
    """Prints the average runtime of the functions passed as arguments"""

    @functools.wraps(func)
    def wrapper_timer(calc_range, repetitions, *functions):

        acumulated_time = {}
        for function in functions:
            acumulated_time[function.__name__] = 0

        for n in range(repetitions):
            for function in functions:
                start_time = time.perf_counter()    # 1
                function(calc_range)
                end_time = time.perf_counter()      # 2
                run_time = end_time - start_time
                acumulated_time[function.__name__] += run_time
                print(f"Executed function {function.__name__} in {run_time:.9f} secs")

        average_time = {}
        for function in functions:
            average_time[function.__name__] = acumulated_time[function.__name__] / repetitions
            print(f"Finished {function.__name__!r} in {average_time[function.__name__]:.8f} secs")

        return functions

    return wrapper_timer


def function1(calc_range):
    l = []
    for x in range(calc_range):
        l.append(x * x)
    print(l)
    return l


def function2(calc_range):
    l = [x * x for x in range(calc_range)]
    print(l)
    return l


@timer
def time_functions(*args):
    return args


calc_range = 100
repetitions = 100
functions = (function1, function2)
time_functions(calc_range, repetitions, function1, function2)

```