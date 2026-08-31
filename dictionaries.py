user = {
    "nama": "Falen",
    "umur": 16,
    "hobi": "Programming",
    "skill": "Python"
}

# Menampilkan semua key
print("Keys:", user.keys())

# Menampilkan semua value
print("Values:", user.values())

# Mengecek apakah key tersedia
print("Apakah ada nama?", "nama" in user)

# Mengambil data dengan get()
print("Nama:", user.get("nama"))