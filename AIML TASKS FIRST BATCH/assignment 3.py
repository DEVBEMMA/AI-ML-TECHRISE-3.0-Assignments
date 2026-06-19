
# Exercise 3 — Your Street as a Data Structure
# below is a list having 8 different tuples, containing values for 8 different buildings.




street_buildings = [
    ("Hotel de la paix", "Commercial", 1974 ),
    ("Oris Club", "Commercial", 2008 ),
    ("Filling Station", "Commercial", 2013 ),
    ("Midtown Plaza", "Commercial", 2004 ),
    ("Cubana club", "Commercial", 2011 ),
    ("Life point IVF center", "Public", 2014 ),
    ("One story building", "Residential", 2019 ),
    ("Tech Hub", "Office", 2018)
]

# finding oldest building:
oldest_building = street_buildings[0]#the program will guess that the index 0 item is the oldest
for building in street_buildings:
    if building[2] < oldest_building[2]:
        oldest_building = building
print(oldest_building)


# all unique building types


building_types = set() #we created a set where we will store unique buildings
for building in street_buildings:
    building_types.add(building[1]) #Due to the facct that sets do not accept printing of duplicate values,
    # it will pick one instance of that value
print(building_types)


# Buildings built after 2000
recent_buildings = []#a list where we will store the buildings built after the year 2000
for building in street_buildings:
    if building[2] > 2000: # if the index 2 being year  is greater than year 2000
        recent_buildings.append(building)
print(recent_buildings)

 # Average age of buildings.
this_year = 2026 #this will aid in calculation
total_age = 0
for building in street_buildings:
    total_age += this_year - building[2]
average_age = total_age / len(street_buildings)
print(average_age)
"""for each building tuple, we minus the building year from our present year to get the age. that
then, to get the avg, we divide the total age we got earlier by the number of buildings in the list.
sum of all ages after subtraction form out current year is 147. 
divided by the number of building tuples (8) will give us the avg 18.375
"""

# A GENERAL REPORT FOR ALL THE OPERATIONS
print("Below is A GENERAL REPORT FOR ALL THE OPERATIONS")
print(f"The oldest building is: {oldest_building[0]} and it was built in {oldest_building[2]}")
print("Unique building types include:", building_types)
print(f"Buildings built after 2000: {recent_buildings}")
print(f"The average age of buildings: {average_age} years")