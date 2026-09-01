import json

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(f"Nama   : {student['nama']}")
    print(f"Kelas  : {student['kelas']}")
    print(f"Umur   : {student['umur']}")
    print(f"Alamat : {student['alamat']}")
    print("-" * 30)