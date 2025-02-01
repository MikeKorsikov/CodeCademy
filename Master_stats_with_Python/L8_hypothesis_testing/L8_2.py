# binomial testing

import numpy as np
from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p, alternative_hypothesis='not_equal'):
    """
    Perform a simulation-based binomial test.
    
    Parameters:
    - observed_successes: Number of observed successes
    - n: Total number of trials
    - p: Probability of success under the null hypothesis
    - alternative_hypothesis: 'less', 'greater', or 'not_equal'
    
    Returns:
    - p-value based on the alternative hypothesis
    """

    # Initialize null_outcomes
    null_outcomes = []

    # Generate the simulated null distribution
    for _ in range(10000):  # Simulating 10,000 trials
        simulated_data = np.random.choice(['y', 'n'], size=n, p=[p, 1 - p])
        num_purchased = np.sum(simulated_data == 'y')
        null_outcomes.append(num_purchased)

    # Convert to NumPy array for efficient computation
    null_outcomes = np.array(null_outcomes)

    # Compute p-value based on alternative hypothesis
    if alternative_hypothesis == 'less':
        p_value = np.sum(null_outcomes <= observed_successes) / len(null_outcomes)
    elif alternative_hypothesis == 'greater':
        p_value = np.sum(null_outcomes >= observed_successes) / len(null_outcomes)
    elif alternative_hypothesis == 'not_equal':
        # Two-tailed test: sum of both tails
        p_lower = np.sum(null_outcomes <= observed_successes) / len(null_outcomes)
        p_upper = np.sum(null_outcomes >= observed_successes) / len(null_outcomes)
        p_value = 2 * min(p_lower, p_upper)  # Two-tailed test doubles the smaller tail probability
    else:
        raise ValueError("alternative_hypothesis must be 'less', 'greater', or 'not_equal'.")

    return p_value

#Test your function:
print('lower tail one-sided test:')
p_value1 = simulation_binomial_test(45, 500, .1, alternative_hypothesis = 'less')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

print('upper tail one-sided test:')
p_value1 = simulation_binomial_test(53, 500, .1, alternative_hypothesis = 'greater')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(53, 500, .1, alternative = 'greater')
print("binom_test p-value: ", p_value2)

print('two-sided test:')
p_value1 = simulation_binomial_test(42, 500, .1, alternative_hypothesis = 'not_equal')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(42, 500, .1)
print("binom_test p-value: ", p_value2)