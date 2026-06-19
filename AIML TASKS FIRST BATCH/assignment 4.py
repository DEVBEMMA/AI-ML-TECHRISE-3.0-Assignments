# Phone contact duplicator
# cleaned_list = []
# duplicates = set()

# for contact in contacts_list:


#15 names, 5 variations or duplicates
contacts_list = ["Emma", "Ema", "FreD", "LuKe", "BONIFACE", "samuel",
                 "aleX", "graCE", "MARk", "JoHn", "luke", "fred", "SAMUEL",
                 "ALEX", "EMMa"]
# we will need to collect the cleaned contact list and the duplicated contact list, so;
cleaned_list = [] #includes normalised case, and duplicates
duplicates = [] #this will house the duplicated names
single = [] #this will only house names thar appear once

#  Write a program that cleans whitespace, normalises case,
for name in contacts_list:
    clean_name = name.strip().lower()#strip() eliminates extra spaces and .lower() normalizes the casing down to lowercase for easy comparison
    cleaned_list.append(clean_name) #this takes all items from clean name and appends to the empty cleaned_list list


# We need to find duplicates and singles
for name in cleaned_list:
    if cleaned_list.count(name) >1: #if any name in cleaned list appears more than once,
        if name not in duplicates:
            duplicates.append(name) #move it to the empty list duplicates

    else:
        if name not in single:
            single.append(name)

print("Cleaned names:", cleaned_list)
print("Duplicate names:", duplicates)
print("The names that occured once:", single)

#     if name in clean_name => 2:
#         duplicates.add(clean_name)
#
#     else:
#         duplicates.add(clean_name)
#
# print("cleaned list: ")
# print(cleaned_list)
#
# print("\n duplicates list: ")
# print(duplicates)