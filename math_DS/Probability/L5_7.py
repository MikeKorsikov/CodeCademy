
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## Setting up our parameters
pop_mean_cod = 36
pop_std_dev = 20
samp_size = 25
sample_mean = 30

standard_error = pop_std_dev / (samp_size)**(1/2)

cod_cdf = stats.norm.cdf(sample_mean, pop_mean_cod, standard_error)