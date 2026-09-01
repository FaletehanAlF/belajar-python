catatan = input("Masukkan catatan: ")

with open("notes.txt", "a") as file:
    file.write(f"{catatan}\n")

print("Catatan berhasil disimpan!")