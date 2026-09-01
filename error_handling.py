try:
    angka = int(input("Masukkan angka: "))
    print("Angka kamu:", angka)

except ValueError:
    print("Input harus berupa angka!")

else:
    print("Input berhasil diproses.")

finally:
    print("Program selesai.")