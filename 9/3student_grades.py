student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆


# creating empty dictionary
student_grades={}

for i in student_scores:
    if student_scores[i]>90:
        student_grades[i]="Oustanding"
    elif student_scores[i]>80:
        student_grades[i]="Exceeds Expectations"
    elif student_scores[i]>70:
        student_grades[i]="Acceptable"
    else:
        student_grades[i]="Fail"

    # or
    
for j in student_scores:
    score=student_scores[j]
    if score>90:
        student_grades[i]="Oustanding"
    elif score>80:
        student_grades[i]="Exceeds Expectations"
    elif score>70:
        student_grades[i]="Acceptable"
    else:
        student_grades[i]="Fail"    

# 🚨 Don't change the code below 👇
print(student_grades)
