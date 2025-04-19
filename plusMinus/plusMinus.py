from hackerrank.utils import time_execution, memory_usage


def get_positive_values(arr):
    return [n for n in arr if n > 0]

    
def get_zero_values(arr):
    return [n for n in arr if n == 0]

    
def get_negative_values(arr):
    return [n for n in arr if n < 0]


@time_execution
@memory_usage
def plusMinus(arr):    
    positive_values = len(get_positive_values(arr))
    negative_values = len(get_negative_values(arr))
    zero_values = len(get_zero_values(arr))

    arr_size = len(arr)

    print(f"{positive_values / arr_size:6f}")
    print(f"{negative_values / arr_size:6f}")
    print(f"{zero_values / arr_size:6f}")


if __name__ == "__main__":
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
