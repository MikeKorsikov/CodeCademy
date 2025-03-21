import openai

# generate API key 


# Step 1 (start chat/ask question)
response = openai.completions.create(
    model="gpt-3.5-turbo",  # Use gpt-3.5-turbo if you don't have access to gpt-4
    prompt="What is the population of Poland as per 2024?",  # The prompt to send to the model
    max_tokens=100  # Optionally set the maximum tokens for the response
)

# Step 2 (print the response)
print(response['choices'][0]['text'])  # Use 'text' instead of 'message'