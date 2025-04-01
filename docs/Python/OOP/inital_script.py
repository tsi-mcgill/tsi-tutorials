import numpy as np
import matplotlib.pyplot as plt

# Create an array of 100x100 random numbers drawn from a gaussian of mean 10 and width 1
data = np.random.normal(loc = 10, scale = 1, size = (1000,10))

data_mean = data.mean()
data_std = data.std()
data_min = data.min()
data_max = data.max()


