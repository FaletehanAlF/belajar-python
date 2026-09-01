import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
    print("File berhasil dihapus.")
else:
    print("File tidak ditemukan.")