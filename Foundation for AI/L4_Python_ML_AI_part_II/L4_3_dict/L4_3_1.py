# dictionaries

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475, "stringQueen": 85739})

print(user_ids)

# Dict Comprehensions
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine  = {key:value for key, value in zipped_drinks}
 
print(drinks_to_caffeine)
