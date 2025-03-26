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

# convert damage values to floats or pass-through notes
def convert_damages(value):
  if value[-1] == 'M':
    stripped_value = value.strip('M')
    converted_value = float(stripped_value) * 1000000
  elif value[-1] == 'B':
    stripped_value = value.strip('B')
    converted_value = float(stripped_value) * 1000000000
  elif value == 'Damages not recorded':
    return value
  else:
    return 'Please enter valid data'
  
  # from values ending with 'M' or 'B'
  return converted_value

# test convert_damages() function
# print('Billion:', convert_damages('100B'))
# print('Million:', convert_damages('100M'))
# print('Billion:', convert_damages('100B'))
# print('Not recorded:', convert_damages('Damages not recorded'))
# print('Error test:', convert_damages('100T'))

# update damages list
updated_damages = []
for value in damages:
  updated_damages.append(convert_damages(value))
# print(updated_damages)

# 2 
# Create a Table

def create_hurricane_dictionary(names, months, years, max_sustained_winds, 
                                areas_affected, updated_damages, deaths):
    """
    Convert hurricane data from separate lists into a nested dictionary.
    
    This function takes multiple lists containing hurricane data and transforms 
    them into a dictionary where each hurricane's name is a key, and the value 
    is another dictionary containing detailed information about that hurricane.
    
    Parameters:
    - names: List of hurricane names
    - months: List of months when hurricanes occurred
    - years: List of years of hurricane occurrence
    - max_sustained_winds: List of maximum sustained wind speeds
    - areas_affected: List of areas impacted by each hurricane
    - updated_damages: List of damage amounts
    - deaths: List of number of deaths caused by each hurricane
    
    Returns:
    A dictionary where each key is a hurricane name, and each value is a 
    dictionary containing detailed hurricane information.
    """
    # Create an empty dictionary to store hurricane information
    hurricanes = {}
    
    # Iterate through the range of hurricane records
    # Using len(names) ensures we process all hurricanes in the dataset
    for index in range(len(names)):
      # Create a dictionary for each individual hurricane
      hurricane_info = {
        "Name": names[index],
        "Month": months[index],
        "Year": years[index],
        "Max Sustained Wind": max_sustained_winds[index],
        "Areas Affected": areas_affected[index],
        "Damage": updated_damages[index],
        "Deaths": deaths[index]
      }
      
      # Use the hurricane name as the key in the main hurricanes dictionary
      # This allows easy access to each hurricane's information
      hurricanes[names[index]] = hurricane_info
  
    # Return the complete dictionary of hurricanes
    return hurricanes

# Create and view the hurricanes dictionary
hurricanes = create_hurricane_dictionary(
  names, months, years, max_sustained_winds, 
  areas_affected, updated_damages, deaths
)
# print one hurricane as test
# print(hurricanes["Cuba I"])
# print fully nested hurricane dictionary
# print(hurricanes)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key

def organize_hurricanes_by_year(hurricanes):
  """
  Reorganize the hurricane dictionary to group hurricanes by their year of occurrence.
  
  Parameters:
  - hurricanes: A dictionary where keys are hurricane names and values are 
                dictionaries containing hurricane information
  
  Returns:
  A dictionary where keys are years and values are lists of hurricane dictionaries 
  that occurred in that year
  """
  # Create an empty dictionary to store hurricanes organized by year
  hurricanes_by_year = {}
  
  # Iterate through each hurricane in the input dictionary
  for hurricane_name, hurricane_info in hurricanes.items():
    # Get the current hurricane's year
    current_year = hurricane_info['Year']
      
    # Check if the year already exists in our new dictionary
    if current_year not in hurricanes_by_year:
      # If the year doesn't exist, create a new list with this hurricane
      hurricanes_by_year[current_year] = [hurricane_info]
    else:
      # If the year exists, append this hurricane to the existing list
      hurricanes_by_year[current_year].append(hurricane_info)
  
  # Return the reorganized dictionary
  return hurricanes_by_year

# Example usage:
hurricanes_by_year = organize_hurricanes_by_year(hurricanes)
# print(hurricanes_by_year[1924])  # Print all hurricanes from 1924
# print(len(hurricanes_by_year[1924]))  # Print number of hurricanes in 1924
# print(hurricanes_by_year) # Print all hurricanes by year

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes there

def count_affected_areas(hurricanes):
  """
  Count how many times each area is affected by hurricanes.
  
  Parameters:
  - hurricanes: A dictionary where keys are hurricane names and values are 
                dictionaries containing hurricane information
  
  Returns:
  A dictionary where keys are affected areas and values are the number 
  of times those areas were impacted by hurricanes
  """
  # Create an empty dictionary to store area frequency
  affected_areas_count = {}
  
  # Iterate through each hurricane in the input dictionary
  for hurricane_name, hurricane_info in hurricanes.items():
    # Get the list of areas affected by the current hurricane
    current_areas = hurricane_info['Areas Affected']
    
    # Count each area in the current hurricane's affected areas
    for area in current_areas:
      # If the area is not yet in the dictionary, initialize its count to 1
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      # If the area is already in the dictionary, increment its count
      else:
        affected_areas_count[area] += 1
  
  # Return the dictionary of area frequencies
  return affected_areas_count

# Example usage:
# First, run the count_affected_areas function
# area_frequencies = count_affected_areas(hurricanes)

# Check how many times Mexico was affected
# mexico_frequency = area_frequencies['Mexico']
# print(f"Mexico was affected by hurricanes {mexico_frequency} times.")

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes there

def find_most_affected_area(hurricanes):
  """
  Determine the area most frequently affected by hurricanes.
  
  Parameters:
  - hurricanes: A dictionary where keys are hurricane names and values are 
                dictionaries containing hurricane information
  
  Returns:
  A tuple containing the most affected area and its number of occurrences
  """
  # Create an empty dictionary to store area frequency
  affected_areas_count = {}
  
  # Iterate through each hurricane in the input dictionary
  for hurricane_name, hurricane_info in hurricanes.items():
    # Get the list of areas affected by the current hurricane
    current_areas = hurricane_info['Areas Affected']
    
    # Count each area in the current hurricane's affected areas
    for area in current_areas:
      # If the area is not yet in the dictionary, initialize its count to 1
      if area not in affected_areas_count:
        affected_areas_count[area] = 1
      # If the area is already in the dictionary, increment its count
      else:
        affected_areas_count[area] += 1
  
  # Find the area with the maximum number of occurrences
  most_affected_area = max(affected_areas_count, key=affected_areas_count.get)
  max_occurrences = affected_areas_count[most_affected_area]
  
  # Return the most affected area and its number of occurrences
  return (most_affected_area, max_occurrences)

# Example usage:
# most_affected = find_most_affected_area(hurricanes)
# print(f"The most affected area is {most_affected[0]}, "
#       f"hit by hurricanes {most_affected[1]} times.")

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

def find_deadliest_hurricane(hurricanes):
  """
  Determine the hurricane that caused the greatest number of deaths.
  
  Parameters:
  - hurricanes: A dictionary where keys are hurricane names and values are 
                dictionaries containing hurricane information
  
  Returns:
  A tuple containing the name of the deadliest hurricane and its death toll
  """
  # Initialize variables to track the deadliest hurricane
  deadliest_hurricane_name = None
  max_deaths = 0
  
  # Iterate through each hurricane in the input dictionary
  for hurricane_name, hurricane_info in hurricanes.items():
    # Get the number of deaths for the current hurricane
    current_deaths = hurricane_info['Deaths']
    
    # Update the deadliest hurricane if current deaths are higher
    if current_deaths > max_deaths:
      max_deaths = current_deaths
      deadliest_hurricane_name = hurricane_name
  
  # Return the name of the deadliest hurricane and its death toll
  return (deadliest_hurricane_name, max_deaths)

# Example usage:
# deadliest = find_deadliest_hurricane(hurricanes)
# print(f"The deadliest hurricane was {deadliest[0]}, "
#       f"causing {deadliest[1]} deaths.")

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
