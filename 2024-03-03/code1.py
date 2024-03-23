import json

with open(r'C:\baejunwoo\2024-03-03\school.json', 'r', encoding='UTF-8') as f:
    buffer = f.read()
    school_list = json.loads(buffer)
    school_list = school_list[0]

    students = set()
    for student in school_list['students']:
        students.add(student['name'])

print(students)