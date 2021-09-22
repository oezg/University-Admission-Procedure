admission_num = int(input())
applicants_file = open("applicant_list_7.txt", "r", encoding="utf-8")
applicants_list = [line.rstrip().split() for line in applicants_file.readlines()]
applicants_file.close()
exams = {"Physics": (2, 4),
         "Biotech": (2, 3),
         "Chemistry": (3,),
         "Mathematics": (4,),
         "Engineering": (4, 5),
         }
departments = {department: [] for department in sorted(exams)}
for i in range(7, 10):
    for department, students in departments.items():
        free_places = admission_num - len(students)
        if free_places > 0:
            candidates = [applicant for applicant in applicants_list if applicant[i] == department]
            candidates.sort(key=lambda x: (-max(int(x[6]), sum(int(x[column]) for column in exams[department]) / len(exams[department])), x[0], x[1]))
            for place in range(free_places):
                try:
                    students.append(candidates[place])
                except IndexError:
                    break
                else:
                    students.sort(key=lambda x: (-max(int(x[6]), sum(int(x[column]) for column in exams[department]) / len(exams[department])), x[0], x[1]))
                    applicants_list.remove(candidates[place])
for department, students in departments.items():
    file_name = department.lower()+".txt"
    with open(file_name, "w", encoding="utf-8") as department_file:
        for student in students:
            print(student[0], student[1], max(int(student[6]), sum(int(student[column]) for column in exams[department]) / len(exams[department])),
                  file=department_file)

