# project

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
print(f"\nExercise 1:")
def convert_damages(damages):
    conversion = {"M": 1_000_000, "B": 1_000_000_000}
    converted_damages = []
    
    for damage in damages:
        if damage == "Damages not recorded":
            converted_damages.append(damage)
        else:
            value, unit = damage[:-1], damage[-1]  # Extract number and unit (M/B)
            converted_damages.append(float(value) * conversion[unit])  # Convert to float
            
    return converted_damages

# Test the function
updated_damages = convert_damages(damages)
print(updated_damages)


# 2 
# Create a Table
print(f"\nExercise 2:")
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}

    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": updated_damages[i],
            "Deaths": deaths[i]
        }

    return hurricanes

# Create and view the hurricanes dictionary
hurricane_dict = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricane_dict)

# 3
# Organizing by Year
print(f"\nExercise 3:")
# Organize hurricanes by year
def organize_by_year(hurricane_dict):
    hurricanes_by_year = {}

    for hurricane in hurricane_dict.values():  # Iterate over hurricane data
        year = hurricane["Year"]
        
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []  # Create list if year doesn't exist
        
        hurricanes_by_year[year].append(hurricane)  # Append hurricane data to the year

    return hurricanes_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_by_year(hurricane_dict)
print(hurricanes_by_year)

# 4
# Counting Damaged Areas
print(f"\nExercise 4:")
# Count how often each area was affected
def count_affected_areas(hurricane_dict):
    affected_counts = {}

    for hurricane in hurricane_dict.values():  # Loop through hurricanes
        for area in hurricane["Areas Affected"]:  # Loop through affected areas
            if area not in affected_counts:
                affected_counts[area] = 1  # Initialize count
            else:
                affected_counts[area] += 1  # Increment count

    return affected_counts

# create dictionary of areas to store the number of hurricanes involved in
affected_area_counts = count_affected_areas(hurricane_dict)
print(affected_area_counts)

# 5 
# Calculating Maximum Hurricane Count
print(f"\nExercise 5:")
def most_affected_area(affected_area_counts):
    max_area = max(affected_area_counts, key=affected_area_counts.get)  # Find the area with max occurrences
    return max_area, affected_area_counts[max_area]  # Return area and count

# find most frequently affected area and the number of hurricanes involved in
most_affected, times_hit = most_affected_area(affected_area_counts)
print(f"The most affected area is {most_affected}, hit {times_hit} times.")

# 6
# Calculating the Deadliest Hurricane
print(f"\nExercise 6:")
def deadliest_hurricane(hurricane_dict):
    deadliest = max(hurricane_dict.values(), key=lambda h: h["Deaths"])  # Find hurricane with max deaths
    return deadliest["Name"], deadliest["Deaths"]  # Return hurricane name and deaths

# find highest mortality hurricane and the number of deaths
deadliest_name, max_deaths = deadliest_hurricane(hurricane_dict)
print(f"The deadliest hurricane is {deadliest_name}, causing {max_deaths} deaths.")

# 7
# Rating Hurricanes by Mortality
print(f"\nExercise 7:")

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def categorize_by_mortality(hurricane_dict, mortality_scale):
    mortality_categories = {key: [] for key in mortality_scale}  # Initialize categories

    for hurricane in hurricane_dict.values():  # Loop through hurricanes
        deaths = hurricane["Deaths"]
        
        # Determine mortality rating based on scale
        for rating, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                mortality_categories[rating].append(hurricane)  # Assign hurricane to category
                break  # Stop checking after finding the correct category

    return mortality_categories
# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = categorize_by_mortality(hurricane_dict, mortality_scale)
for rating, hurricanes in hurricanes_by_mortality.items():
    print(f"Mortality Rating {rating}: {len(hurricanes)} hurricanes")

# 8 Calculating Hurricane Maximum Damage
print(f"\nExercise 8:")
def most_costly_hurricane(hurricane_dict):
    costly_hurricanes = [
        h for h in hurricane_dict.values() if isinstance(h["Damage"], (int, float))
    ]  # Filter out hurricanes without recorded damage
    
    if not costly_hurricanes:
        return "No valid data available."

    most_costly = max(costly_hurricanes, key=lambda h: h["Damage"])  # Find hurricane with max damage
    return most_costly["Name"], most_costly["Damage"]

# find highest damage inducing hurricane and its total cost
costliest_name, max_damage = most_costly_hurricane(hurricane_dict)
print(f"The most costly hurricane is {costliest_name}, causing ${max_damage:,} in damages.")

# 9
# Rating Hurricanes by Damage
print(f"\nExercise 9:")
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def categorize_by_damage(hurricane_dict, damage_scale):
    damage_categories = {key: [] for key in damage_scale}  # Initialize categories

    for hurricane in hurricane_dict.values():  # Loop through hurricanes
        damage = hurricane["Damage"]
        
        # Only process hurricanes with numerical damage values
        if isinstance(damage, (int, float)):
            for rating, upper_bound in damage_scale.items():
                if damage <= upper_bound:
                    damage_categories[rating].append(hurricane)  # Assign hurricane to category
                    break  # Stop checking after finding the correct category

    return damage_categories

# categorize hurricanes in new dictionary with damage severity as key
hurricanes_by_damage = categorize_by_damage(hurricane_dict, damage_scale)

# Print summary
for rating, hurricanes in hurricanes_by_damage.items():
    print(f"Damage Rating {rating}: {len(hurricanes)} hurricanes")