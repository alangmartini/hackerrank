import multiprocessing as mp
from ..utils import time_execution, memory_usage
from functools import partial

def count_values(condition, arr):
    return sum(1 for n in arr if condition(n))


def is_positive(x):
    return x > 0


def is_negative(x):
    return x < 0


def is_zero(x):
    return x == 0

@time_execution
@memory_usage
def plusMinus(arr):
    with mp.Pool(processes=3) as pool:
        conditions = [
            is_positive, is_zero, is_negative
        ]

        count_func = partial(count_values, arr=arr)

        results = pool.map(count_func, conditions)

        positive_count, negative_count, zero_count = results

        arr_size = len(arr)

        print(f"{positive_count / arr_size:6f}")
        print(f"{negative_count / arr_size:6f}")
        print(f"{zero_count / arr_size:6f}")

        return


if __name__ == "__main__":
    #freeze_suport()
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
