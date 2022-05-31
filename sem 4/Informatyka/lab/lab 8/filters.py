import numpy as np


def own_method(one, two):
    # average = 0
    # div_sum = 0
    pixels_num = one.shape[0] * one.shape[1] * 3
    # for i in range(len(one)):
    #     for j in range(len(one[i])):
    #         for k in range(len(one[i][j])):
    #             div_sum = div_sum + abs(int(one[i][j][k]) - int(two[i][j][k]))
    # average = div_sum / pixels_num

    sum_1_2 = np.subtract(one, two)
    abs_1_2 = np.abs(sum_1_2)

    abs_sum = np.sum(abs_1_2, axis=2)
    abs_sum = np.sum(abs_sum, axis=1)
    abs_sum = np.sum(abs_sum)

    average2 = abs_sum / pixels_num
    # print(average)
    # print(average2)
    return average2


def avg(x) -> float:
    return sum(x)/len(x)
