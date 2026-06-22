# Exer. 3 Student Performance Ranking System Topics
# Exercise 3 — Student Performance Ranking System Topics: Functions · Lists · Nested Loops · If statements Create these functions: - `calculate_average(scores_list)` — returns average of a list of scores. 
# - `get_grade(average)` — returns letter grade + remark using if-elif. - `rank_students(student_data)` — where `student_data` is a list of tuples `(name, [score1, score2, score3, score4])`. 
# The ranking function should: - Calculate average and grade for each student. - Sort students by average (descending) using nested loops (no built-in sort). 
# - Print a ranked table with position, name, average, and grade.
def calculate_average(scores_list): #returns average of a list of scores. average = sum(scores_list) / len(scores_list)... (add up all the scores, then divide by how many there are.)
    total = sum(scores_list)
    average = total / len(scores_list)
    return average
    
def get_grade(average):#this will retuen letter grade and remark for each of the grades using if-elif
    if average >= 70:
        return "A","Excellent"
    elif average >=60:
        return "B","Good"
    elif average >=50:
        return "C" , "Satisfactory"
    elif average >=40:
        return "D" ,"Pass"
    else:
        return "F","Fail"
    
#here we try to calculate average and grade for every student and then store it together:
def rank_students(student_data): #where student_data is a list of tuples (name, [score1, score2, score3, score4]. this means that each student will have 4 different scores
    student_result=[] # this will hold (name, average, grade, remark) for each student
    for name, scores in student_data:
        average= calculate_average(scores) #average will refer to the function calculate_average.
        grade, remark =get_grade(average)#when average has been calculated, the grading conditional statements can now kick in.

        student_result.append((name, average, grade, remark))# student_result will be able to take all values from name placehohder, avg, grade and also respective remarks 


# In order to sort the results in descendig order
    num_of_students = len(student_result)#this is the length of tuples in student_result. one tuple per student-- the number of students we have will reflect in the number 
    # of tuples that will show up in student_result. the number of items w num_of_students
    for each_student in range(num_of_students):#for each student in the range 0-the num_of_students. 
        for x in range(num_of_students-1-each_student): #for each comparison of two values. this will compare each pair of neighboring students.eg a vs b then b vs c etc.

            # now remember, student_result now has (name, average, grade,remark).
            if student_result[x][1] < student_result[x+1][1]: #remember each item has (name, average, grade, remark), so index 1 grabs the average for comparison. 
                # if the current student's average is less than the next one's, they're in the wrong order for descending order, so we swap
                student_result[x], student_result[x+1]= student_result[x+1], student_result[x] #this means, switch places. A neat way to swap two values in one line
                

    print(f"{"Position":<10}{'Name':<15}{'Average':<10}{'Grade'}")
    for position, (name, average, grade, remark) in enumerate (student_result, start=1):
        print(f"{position:<10}{name:<15}{average:<10.2f}{grade} ({remark})")

def main_data():
    student_data = [
        ("Michael", [80, 90, 70, 85]),
        ("Obi", [60, 65, 70, 75]),
        ("Chika", [95, 92, 98, 91]),
        ("Ada", [40, 35, 50, 45]),
    ]
    rank_students(student_data)


main_data()

























