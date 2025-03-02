
# project on distributions
import numpy as np
import matplotlib.pyplot as plt

# Given survey responses
survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 
                    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 
                    'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# Step 2: Count total votes for Ceballos
total_ceballos = survey_responses.count("Ceballos")
print(f"Total votes for Ceballos in the survey: {total_ceballos}")

# Step 3: Calculate the percentage of people who voted for Ceballos
total_respondents = len(survey_responses)
percentage_ceballos = total_ceballos / total_respondents * 100
print(f"Percentage of survey respondents who voted for Ceballos: {percentage_ceballos:.2f}%")

# Step 4: Simulate election results using binomial distribution
# In the actual election, 54% of people voted for Ceballos
possible_surveys = np.random.binomial(total_respondents, 0.54, size=10000) / total_respondents
print("\nSimulating 10,000 possible surveys based on actual election results...")

# Step 5: Plot the distribution of survey results
plt.hist(possible_surveys, range=(0, 1), bins=20, edgecolor='black')
plt.title("Distribution of Simulated Survey Results")
plt.xlabel("Proportion of Votes for Ceballos")
plt.ylabel("Frequency")
plt.show()

# Step 6: Calculate the probability that a survey would show Ceballos losing
ceballos_loss_surveys = np.mean(possible_surveys < 0.5) * 100
print(f"Probability of a survey incorrectly predicting a Kerrigan win: {ceballos_loss_surveys:.2f}%")

# Step 7: Simulating a survey with 7,000 respondents
large_survey = np.random.binomial(7000, 0.54, size=10000) / 7000
print("\nSimulating 10,000 possible surveys with a larger sample size of 7,000 respondents...")

# Step 8: Calculate the probability of a survey predicting a Kerrigan win with a larger sample
ceballos_loss_new = np.mean(large_survey < 0.5) * 100
print(f"Probability of a survey incorrectly predicting a Kerrigan win with a larger sample: {ceballos_loss_new:.2f}%")

# Final recommendation
print("\nAnalysis Conclusion:")
if ceballos_loss_new < ceballos_loss_surveys:
    print("A larger sample size significantly improves the accuracy of the survey.")
else:
    print("The survey still shows a high probability of an incorrect prediction, even with a larger sample.")

print("Recommendation: To improve prediction accuracy, increase the number of survey respondents.")
