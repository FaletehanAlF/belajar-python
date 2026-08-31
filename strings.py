nama = "falen"
teknologi = "python"
pesan = "Saya sedang belajar Python setiap hari"

print("=== PROFILE ===")
print(f"Nama: {nama.title()}")
print(f"Teknologi: {teknologi.upper()}")
print(f"Jumlah karakter pesan: {len(pesan)}")

print("\n=== TEXT PROCESSING ===")
print("Huruf kecil:", pesan.lower())
print("Ganti Python:", pesan.replace("Python", "Django"))
print("Apakah ada kata belajar?", "belajar" in pesan)