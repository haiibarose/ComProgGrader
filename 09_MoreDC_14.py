filename1 = input()
filename2 = input()
filename3 = input()

courses_file = open(filename1, 'r')
teachers_file = open(filename2, 'r')
databases_file = open(filename3, 'r')

courses = dict()
teachers = dict()
ans = dict()

for course in courses_file.readlines():
    no, id = course.strip().split(',')
    courses[no] = id
for teacher in teachers_file.readlines():
    no, name = teacher.strip().split(',')
    teachers[no] = name
for database in databases_file.readlines():
    course_no, name_no = database.strip().split(',')
    if (course_no not in courses) or (name_no not in teachers):
        print('record error')
    else:
        print(f"{courses[course_no]}, {teachers[name_no]}")
courses_file.close()
teachers_file.close()
databases_file.close()