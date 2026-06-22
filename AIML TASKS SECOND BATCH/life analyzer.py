# Exercise 2 — Smart Age & Life Stage Analyzer
# Topics: Functions · Loops · If-elif-else · Tuples

# Write a function `analyze_age(dob_tuple)` where `dob_tuple = (day, month, year)`.  
# Inside it:
# - Calculate exact age in years, months, and days (as of current date — hardcode today’s date).
# - Use if-elif chains to determine life stage (Child, Teen, Young Adult, Adult, Senior, etc.).
# - Return a detailed report string.
# - Create another function `compare_ages(person_list)` that takes a list of (name, dob_tuple) and finds the oldest and youngest person using loops.

# Test with at least 5 family members.

# dates_of_birth=[
#     (12, 11, 2000)
#     (22, 4, 2005)
#     (23, 10, 2001)
#     (7, 8, 1999)
#     (17, 1, 1998)
# ] 
today= (22, 6, 2026)

def analyze_age(dob_tuple):
    day,month, year = dob_tuple #here the tuple has been unpacked
    today_day, today_month, today_year = today  #today as a tuple, also unpacked
# Calculate age in years, months, days
    years= today_year-year

    months= today_month-month

    days= today_day-day

    # conditionals for different life stages
    if years < 13:
        stage = "Child"
    elif years < 20:
        stage = "Teen"
    elif years < 30:
        stage = "Young Adult"
    elif years < 60:
        stage = "Adult"
    else:
        stage = "Senior"



    if days < 0:
        days += 30   # assume 30 days in a month
        months -= 1
    if months < 0:
        months += 12
        years -= 1
# if the days calculation goes appears to be negative, add 30 days and subtract 1 month.
# If the months calculation goes negative, add 12 months and subtract 1 year.

# This is just a way of “borrowing” from months and years to keep the age values positive 

# the code below returns the report.

    return f"Age: {years} years, {months} months, {days} days — Life Stage: {stage}"    
# Function to compare ages of people

def compare_ages(person_list): #person list serves as a parameter. when we call the compare_ages funct, we will pass our argument.
    # let us assume the first person is both oldest and youngest
    oldest = person_list[0]
    youngest = person_list[0]

    for person in person_list:
        name, dob = person
        # Calculate age in years only for comparison
        age_years = today[2] - dob[2]

        # Adjust if birthday not yet reached this year
        if (dob[1], dob[0]) > (today[1], today[0]):
            age_years -= 1

        # Compare with oldest
        oldest_age_years = today[2] - oldest[1][2]
        if (dob[1], dob[0]) > (today[1], today[0]):
            oldest_age_years -= 1
        if age_years > oldest_age_years:
            oldest = person

        # Compare with youngest
        youngest_age_years = today[2] - youngest[1][2]
        if (dob[1], dob[0]) > (today[1], today[0]):
            youngest_age_years -= 1
        if age_years < youngest_age_years:
            youngest = person

    return f"Oldest: {oldest[0]}, Youngest: {youngest[0]}"


# Testing with family members ---
family = [
    ("Emmanuel", (15, 4, 2000)),
    ("Samuel", (10, 8, 2010)),
    ("Michael", (25, 12, 1985)),
    ("Sarah", (5, 1, 1999)),
    ("David", (30, 9, 2018))
]

#analysis for each person
for name, dob in family:
    print(name, "-", analyze_age(dob))

# Compare oldest and youngest
print(compare_ages(family))


