student_scores = input("Input a list of students scores: ").split()
for n  in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

heigst=0
for scores in student_scores:
    if heigst < scores:
        heigst= scores

print(f"the heigst scor is : {heigst}")