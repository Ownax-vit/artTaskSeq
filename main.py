import time
import sys
from functools import wraps
from statistics import mean

import matplotlib.pyplot as plt

time_dict = {}


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        runtime = time.time() - start

        if not func.__name__ in time_dict:
            time_dict[func.__name__] = {}

        time_dict[func.__name__][args[0]] = runtime

    return inner


@timer
# способ 1
def print_repeat_digit(n: int) -> None:
    for i in range(n+1):
        print(str(i) * i, end="--\n\n\n")


@timer
# способ 2
def print_repeat_digit2(n: int) -> None:
    res = [str(m) * m for m in range(n+1)]
    print("".join(res))


if __name__ == '__main__':
    funcs = [print_repeat_digit, print_repeat_digit2]

    for i in range(0, 3000, 100):
        for func in funcs:
            func(i)

    for k, v in time_dict.items():

        labels = sorted(time_dict[k].keys())
        value = sorted(time_dict[k].values())
        res_sum = mean(value)

        plt.title(f"Function:{k} Mean:{res_sum}")
        plt.xlabel('n')
        plt.ylabel('time s')
        plt.plot(labels, value)
        plt.grid(True)
        plt.show()
