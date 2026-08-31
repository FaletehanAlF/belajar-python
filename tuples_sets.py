teknologi = {"Python", "JavaScript", "Java"}

# Menambahkan data
teknologi.add("Go")

print("Setelah ditambahkan:", teknologi)

# Menghapus data
teknologi.remove("Java")

print("Setelah dihapus:", teknologi)

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "JavaScript", "PHP"}

# Data yang ada di kedua Set
print("Teknologi yang sama:", frontend & backend)

# Menggabungkan semua data tanpa duplikat
print("Semua teknologi:", frontend | backend)

# Data yang hanya ada di frontend
print("Hanya frontend:", frontend - backend)