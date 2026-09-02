import json

with open("students.json", "r") as file:
    students = json.load(file)


nama = input("Masukkan nama: ")
kelas = input("Masukkan kelas: ")
umur = int(input("Masukkan umur: "))

new_student = {
    "id": len(students) + 1,
    "nama": nama,
    "kelas": kelas,
    "umur": umur
}

students.append(new_student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Siswa berhasil ditambahkan!")