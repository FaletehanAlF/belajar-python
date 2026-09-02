import json


with open("students.json", "r") as file:
    students = json.load(file)


while True:
    print("\n=== STUDENT MANAGEMENT ===")
    print("1. Lihat semua siswa")
    print("2. Tambah siswa")
    print("3. Cari siswa")
    print("4. Update siswa")
    print("5. Hapus siswa")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n=== DAFTAR SISWA ===")

        if not students:
            print("Belum ada data siswa.")
        else:
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
        nama = input("Masukkan nama siswa yang dicari: ")

        found = False

        for student in students:
            if student["nama"].lower() == nama.lower():
                print("\n=== SISWA DITEMUKAN ===")
                print(f"ID     : {student['id']}")
                print(f"Nama   : {student['nama']}")
                print(f"Kelas  : {student['kelas']}")
                print(f"Umur   : {student['umur']}")

                found = True

        if not found:
            print("Siswa tidak ditemukan.")

    elif pilihan == "4":
        id_siswa = int(input("Masukkan ID siswa yang ingin diupdate: "))

        found = False

        for student in students:
            if student["id"] == id_siswa:
                print("\n=== UPDATE SISWA ===")

                nama = input("Masukkan nama baru: ")
                kelas = input("Masukkan kelas baru: ")
                umur = int(input("Masukkan umur baru: "))

                student["nama"] = nama
                student["kelas"] = kelas
                student["umur"] = umur

                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("Data siswa berhasil diupdate!")

                found = True
                break

        if not found:
            print("Siswa tidak ditemukan.")

    elif pilihan == "5":
        id_siswa = int(input("Masukkan ID siswa yang ingin dihapus: "))

        found = False

        for student in students:
            if student["id"] == id_siswa:
                students.remove(student)

                with open("students.json", "w") as file:
                    json.dump(students, file, indent=4)

                print("Siswa berhasil dihapus!")

                found = True
                break

        if not found:
            print("Siswa tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")