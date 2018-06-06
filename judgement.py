from DataSampling import load_data
from random import randint


def condition():
    if randint(0, 10) > 5:
        return True
    return False


def judgementSampling(data, n):
    i = 0
    sample = []
    for dt in data:
        if i >= n:
            break
        if condition():
            sample.append(dt)
            i += 1
    return sample


data, label = load_data('iris.csv')
print(data)
print(judgementSampling(data, 5))
