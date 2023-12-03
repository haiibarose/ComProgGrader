ids = list()
grades = list()
letter_grades = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

while True:
    code = input()
    if code == 'q':
        break
    id, grade = code.split()
    ids.append(id)
    grades.append(grade)
uids = input().split()

for uid in uids:
    grades[ids.index(uid)] = letter_grades[letter_grades.index(grades[ids.index(uid)])+1]

for id, grade in zip(ids, grades):
    print(id, grade)