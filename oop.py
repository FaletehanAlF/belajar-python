class User:
    def __init__(self, nama, umur, email, password):
        self.nama = nama
        self.umur = umur
        self.__email = email
        self.__password = password

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}")
        print(f"Umur saya {self.umur} tahun")

    def tambah_umur(self, jumlah):
        self.umur += jumlah

    def get_info(self):
        return f"{self.nama} berusia {self.umur} tahun"

    def is_adult(self):
        return self.umur >= 18

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password


class Developer(User):
    def bekerja(self):
        print(f"{self.nama} sedang coding")


class Designer(User):
    def bekerja(self):
        print(f"{self.nama} sedang membuat desain")


class Teacher(User):
    def bekerja(self):
        print(f"{self.nama} sedang mengajar")


# Membuat object
user1 = User(
    "Falen",
    16,
    "falen@example.com",
    "python123"
)

developer = Developer(
    "Falen",
    16,
    "developer@example.com",
    "dev123"
)

designer = Designer(
    "Kimmy",
    24,
    "designer@example.com",
    "design123"
)

teacher = Teacher(
    "Andi",
    30,
    "teacher@example.com",
    "teacher123"
)


# Method User
user1.perkenalan()

user1.tambah_umur(1)

print(user1.get_info())
print("Sudah dewasa:", user1.is_adult())


# Encapsulation
print("Email:", user1.get_email())

user1.set_email("falen@gmail.com")

print("Email baru:", user1.get_email())


# Polymorphism
users = [
    developer,
    designer,
    teacher
]

for user in users:
    user.bekerja()