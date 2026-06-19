"""
Create a set of all students in your class (at least 10 names).
 Then create separate sets for students who attended Monday, Tuesday,and Wednesday.
 Use set operations to find who attended all 3 days,
 who missed at least one, who only came once, and who never attended at all.

"""

# A set is student names.
students = {"Emmanuel", "Tunde", "Ada", "Chika", "Bola", "Ngozi", "Ifeanyi", "Kemi", "John", "Blessing"}

# Create sets for attendance on each day
# Each set contains the names of students who attended that day.
monday_attendance = {"Emmanuel", "Ada", "Dera", "Michael" "John"}
tuesday_attendance = {"Tunde", "Ada", "Bola", "Ngozi", "Blessing"}
wednesday_attendance = {"Emmanuel", "Tunde", "Ada", "Kemi", "Blessing"}

# to find those who attended for all days

complete_attendance = monday_attendance & tuesday_attendance & wednesday_attendance
print(complete_attendance)

# to find students who missed at least one day

#  all students minus those who attended all days.
incomplete_attendance = students - complete_attendance
print(incomplete_attendance)

# For us to students who only came once
# First, we combine all attendance into one big set (union).
all_attendance = monday_attendance | tuesday_attendance | wednesday_attendance
print(all_attendance)
attended_once = {name for name in all_attendance if (name in monday_attendance) + (name in tuesday_attendance) + (name in wednesday_attendance) + (name in wednesday_attendance)==1}
"""
the above means, name will be assigned to attended_once if the occurence of name cumulatively =1
"""

# For the student who never attended classes
never_attended =  students - all_attendance
print(f"students who never attended include: {never_attended}")


# results
print("Students who attended all 3 days:", complete_attendance)
print("Students who missed at least one day:", incomplete_attendance)
print("Students who only came once:", attended_once)
print("Students who never attended:", never_attended)
