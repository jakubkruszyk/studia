import numpy as np


def own_method(test, reference):
    pixels_num = test.shape[0] * test.shape[1] * test.shape[2]
    sum_1_2 = np.subtract(test.astype("float32"), reference.astype("float32"))
    abs_1_2 = np.abs(sum_1_2)
    abs_sum = np.sum(abs_1_2)
    average = abs_sum / pixels_num
    return average


def avg(x) -> float:
    if x:
        return sum(x)/len(x)
    else:
        return 0
