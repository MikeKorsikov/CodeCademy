# renaming columns I
df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

# renaming columns II
df.rename(columns={'name': 'movie_title'}, inplace=True)
print(df)

# 
orders = pd.read_csv('shoefly.csv')

#1
print(orders.head())

#2
orders['shoe_source'] = orders.shoe_material.apply(lambda shoe_material: 'animal' if shoe_material == 'leather' else 'vegan')

print(orders)

#3
orders['salutation'] = orders.apply(lambda row: \
                                    'Dear Mr. ' + row['last_name']
                                    if row['gender'] == 'male'
                                    else 'Dear Ms. ' + row['last_name'],
                                    axis=1)
                                    
print(orders)
