import pandas as pd


#2
print("\nExercise 2:")
# Load the dataset
jeopardy = pd.read_csv('Codecademy\Foundation for AI\L6_Pandas\L6_3_dataframes\jeopardy.csv')
# Strip whitespace from all column names
jeopardy.columns = jeopardy.columns.str.strip()

# Verify the cleaned columns
print(jeopardy.columns.tolist())

# Inspect the first few rows
print(jeopardy.head())

# Check column names
print(jeopardy.columns)

#3
print("\nExercise 3:")
def filter_questions(df, words):
    """
    Filters DataFrame for questions containing all words in the list (case insensitive)
    """
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    
    # Check if all words appear in each question
    mask = df['Question'].apply(lambda question: all(
        word in question.lower() 
        for word in words
    ))
    
    return df[mask]

# Test with "King" and "England"
king_england = filter_questions(jeopardy, ["King", "England"])
print(king_england[['Question']].head())
print(f"Number of questions: {len(king_england)}")

#4
print("\nExercise 4:")
def filter_questions_improved(df, words):
    # Check if all words are present in the question (case insensitive)
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    return df.loc[df["Question"].apply(filter)]

# Test the improved function
king_england_improved = filter_questions_improved(jeopardy, ["King", "England"])
print("\nSample questions (improved matching):")
print(king_england_improved[['Question']].head())
print(f"Number of questions (improved): {len(king_england_improved)}")

#5
print("\nExercise 5:")
# Clean the Value column
jeopardy['Value_Float'] = jeopardy['Value'].str.replace('$', '', regex=True).str.replace(',', '', regex=True)
jeopardy['Value_Float'] = pd.to_numeric(jeopardy['Value_Float'], errors='coerce')
jeopardy['Value_Float'] = jeopardy['Value_Float'].fillna(0)

# Analyze difficulty of "King" questions
king_questions = filter_questions_improved(jeopardy, ["King"])
avg_value = king_questions['Value_Float'].mean()
print(f"\nAverage value of questions containing 'King': ${avg_value:.2f}")

#6
print("\nExercise 6:")
def count_unique_answers(df):
    """
    Returns a Series with counts of each unique answer
    """
    return df['Answer'].value_counts()

# Example usage with "King" questions
king_answer_counts = count_unique_answers(king_questions)
print("\nTop 10 answers for 'King' questions:")
print(king_answer_counts.head(10))

#7
print("\nExercise 7:")
# Additional analyses

# 1. Temporal analysis
jeopardy['Air Date'] = pd.to_datetime(jeopardy['Air Date'])
jeopardy['Year'] = jeopardy['Air Date'].dt.year

# Questions by decade
jeopardy['Decade'] = (jeopardy['Year'] // 10) * 10
computer_by_decade = jeopardy[jeopardy['Question'].str.contains('computer', case=False)].groupby('Decade').size()
print("\nComputer questions by decade:")
print(computer_by_decade)

# 2. Category analysis by round
# Limit the scope of the data to reduce memory usage
limited_jeopardy = jeopardy[['Round', 'Category']].dropna()

# Perform the groupby and unstack operation on the limited data
category_by_round = jeopardy.groupby(['Round', 'Category']).size().unstack(fill_value=0)

print("\nCategory frequency by round (sample):")
print(category_by_round.iloc[:5, :5])
