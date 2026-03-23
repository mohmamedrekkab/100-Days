student_heights  = input("Input a list of student heights ").split()
etudient=0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    nbr_etudients += 1
print(student_heights)
total=0
for n in range(0, len(student_heights)):
    total += student_heights[n]
print(total)
avg = total / nbr_etudients
print(f"Average height rounded to the nearest whole number = {avg}")
