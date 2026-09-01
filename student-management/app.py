import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"ID     : {student['id']}")
    print(f"Nama   : {student['nama']}")
    print(f"Kelas  : {student['kelas']}")
    print(f"Umur   : {student['umur']}")
    print("-" * 30)