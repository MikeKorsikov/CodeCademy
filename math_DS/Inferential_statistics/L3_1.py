# significance threshold

# Null: The probability that a learner gets the question correct is 70%.
# Alternative: The probability that a learner gets the question correct is not 70%.

sing_threshhold = 0.05
expected_mean = 0.7

pval = 0.013

if pval < sing_threshhold:
    print(f"Reject null, {pval} is significant.")
else:
    print(f"Do not reject null, {pval} is not significant.")