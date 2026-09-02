import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_mysql"
)

cursor = db.cursor()


while True:
    print("\n=== USER MANAGEMENT ===")
    print("1. Lihat semua user")
    print("2. Tambah user")
    print("3. Cari user")
    print("4. Update user")
    print("5. Hapus user")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        cursor.execute("SELECT * FROM users")

        users = cursor.fetchall()

        print("\n=== DAFTAR USER ===")

        if not users:
            print("Belum ada user.")
        else:
            for user in users:
                print(f"ID     : {user[0]}")
                print(f"Nama   : {user[1]}")
                print(f"Email  : {user[2]}")
                print("-" * 30)

    elif pilihan == "2":
        nama = input("Masukkan nama: ")
        email = input("Masukkan email: ")

        sql = "INSERT INTO users (nama, email) VALUES (%s, %s)"
        values = (nama, email)

        cursor.execute(sql, values)
        db.commit()

        print("User berhasil ditambahkan!")

    elif pilihan == "3":
        id_user = int(input("Masukkan ID user: "))

        sql = "SELECT * FROM users WHERE id = %s"
        values = (id_user,)

        cursor.execute(sql, values)

        user = cursor.fetchone()

        if user:
            print("\n=== USER DITEMUKAN ===")
            print(f"ID     : {user[0]}")
            print(f"Nama   : {user[1]}")
            print(f"Email  : {user[2]}")
        else:
            print("User tidak ditemukan.")

    elif pilihan == "4":
        id_user = int(input("Masukkan ID user yang ingin diupdate: "))
        nama = input("Masukkan nama baru: ")
        email = input("Masukkan email baru: ")

        sql = "UPDATE users SET nama = %s, email = %s WHERE id = %s"
        values = (nama, email, id_user)

        cursor.execute(sql, values)
        db.commit()

        if cursor.rowcount > 0:
            print("User berhasil diupdate!")
        else:
            print("User tidak ditemukan.")

    elif pilihan == "5":
        id_user = int(input("Masukkan ID user yang ingin dihapus: "))

        sql = "DELETE FROM users WHERE id = %s"
        values = (id_user,)

        cursor.execute(sql, values)
        db.commit()

        if cursor.rowcount > 0:
            print("User berhasil dihapus!")
        else:
            print("User tidak ditemukan.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")


cursor.close()
db.close()