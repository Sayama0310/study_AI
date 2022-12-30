#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


def load_data(seed=1984, data_number=100, class_number=3):
    np.random.seed(seed)
    DIM = 2  # dimension of data

    x = np.zeros((data_number * class_number, DIM))
    t = np.zeros((data_number * class_number, class_number), dtype=np.int16)

    for j in range(class_number):
        for i in range(data_number):
            rate = i / data_number
            radius = rate
            theta = j * 4.0 + 4.0 * rate + np.random.randn() * 0.2

            ix = data_number * j + i
            x[ix] = np.array([
                radius * np.sin(theta),
                radius * np.cos(theta),
            ]).flatten()
            t[ix, j] = 1

    return x, t


if __name__ == "__main__":
    data_number = 200
    class_number = 4
    x, t = load_data(1997, data_number, class_number)
    print('x', x.shape)
    print('t', t.shape)

    markers = ['o', 'x', '^', '*']

    for i in range(class_number):
        plt.scatter(
            x[i * data_number:(i + 1) * data_number, 0],
            x[i * data_number:(i + 1) * data_number, 1],
            s=40,
            marker=markers[i],
        )

    plt.show()
