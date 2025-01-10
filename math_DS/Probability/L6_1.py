from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("Codecademy\math_DS\Probability\spotify_data.csv")

# task 2: preview the dataset
print(spotify_data.head())
print(spotify_data.info())

# task 3: select the relevant column
song_tempos = spotify_data["tempo"]
#print(song_tempos)

# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)

# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, samp_size=30, stat="Mean")

# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, samp_size=30, stat="Minimum")

# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, samp_size=30, stat="Variance")

# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# task 14: calculate the standard error
sample_size = 30
standard_error = population_std / (sample_size **(1/2))

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
prob_less_140 = stats.norm.cdf(140, population_mean, standard_error)
print(f"Probability less than 140: {prob_less_140}")

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
prob_gr_150 = 1 - stats.norm.cdf(150, population_mean, standard_error)
print(f"Probability greater than 150: {prob_gr_150}")

