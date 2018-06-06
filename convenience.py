from DataSampling import load_data


def convenienceSampling(data, n):
    sample = data[:n]
    return sample


data = load_data('iris.csv')
print(convenienceSampling(data, 5))
