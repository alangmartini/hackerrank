from hackerrank.plusMinus.plusMinus import plusMinus as simple
from hackerrank.plusMinus.plusMinus_multiprocessing import plusMinus as multiprocess
import numpy as np

random_with_negative = np.random.randint(-100, 101, size=1000000)

if __name__ == "__main__":
    simple(random_with_negative)
    multiprocess(random_with_negative)