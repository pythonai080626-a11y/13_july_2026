# START

num_stud = int(input('number of students?'))

i = 0
max_grade = 0

while i < num_stud and max_grade < 100:
    i += 1
    grade = int(input('grade?'))
    if grade < 0 or grade > 100:
        print('illegal grade')
    elif grade > max_grade:
        max_grade = grade
print(max_grade)

# STOP