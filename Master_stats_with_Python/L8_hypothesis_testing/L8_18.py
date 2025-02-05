#project AB test

# Step 1
import noshmishmosh

# Step 2
import numpy as np

# Step 4
all_visitors = noshmishmosh.customer_visits

# Step 5
paying_visitors = noshmishmosh.purchasing_customers

# Step 6
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# Step 7
baseline_percent = paying_visitor_count / total_visitor_count * 100

# Step 8
print("Baseline percent:")
print(baseline_percent)

# Step 9
payment_history = noshmishmosh.money_spent

# Step 10
average_payment = np.mean(payment_history)

# Step 11
new_customers_needed = np.ceil(1240 / average_payment)

# Step 12
percentage_point_increase = new_customers_needed / total_visitor_count * 100
print("Percentage point increase:")
print(percentage_point_increase)

# Step 13
mde = percentage_point_increase / baseline_percent * 100

# Step 14
print("Minimum Detectable Effect:")
print(mde)

# Step 16
ab_sample_size = 	490