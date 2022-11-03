python_students = []
#python_students = [['KC',12.6],['AR',17.8],['RK',17.8],['AJ',12],['DSR',12.6]]
#"""
student_scores = []
names = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    python_students.append([name,score])

for n in range(len(python_students)):
    student_scores.append(python_students[n][1])

scores_no_duplicates = sorted(set(student_scores))
score_second_lowest = float(scores_no_duplicates[1])

for n in range(len(python_students)):
    if  python_students[n][1] == score_second_lowest:
        names.append(python_students[n][0])

print('\n'.join(sorted(names)))