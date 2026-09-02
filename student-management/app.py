import json


with open("students.json", "r") as file:
    students = json.load(file)


while True:
    print("\n=== STUDENT MANAGEMENT ===")
    print("1. Lihat semua siswa")
    print("2. Tambah siswa")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n=== DAFTAR SISWA ===")

        for student in students:
            print(f"ID     : {student['id']}")
            print(f"Nama   : {student['nama']}")
            print(f"Kelas  : {student['kelas']}")
            print(f"Umur   : {student['umur']}")
            print("-" * 30)

    elif pilihan == "2":
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

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")