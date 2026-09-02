# Python MySQL CRUD

Program sederhana untuk mengelola data user menggunakan Python dan MySQL.

Project ini dibuat sebagai latihan untuk memahami cara menghubungkan Python dengan database MySQL serta menerapkan operasi CRUD.

## Features

- Melihat semua data user
- Menambahkan user baru
- Mencari user berdasarkan ID
- Mengupdate data user
- Menghapus user
- Menu interaktif melalui terminal

## Technologies

- Python
- MySQL
- mysql-connector-python

## Project Structure

```text
python-mysql/
├── app.py
└── README.md

Database

Project ini menggunakan database MySQL dengan nama:

python_mysql

Table yang digunakan:

users
Table Structure
Field	Type	Description
id	INT	ID user
nama	VARCHAR(100)	Nama user
email	VARCHAR(100)	Email user

Field id menggunakan AUTO_INCREMENT dan menjadi PRIMARY KEY.

CRUD Operations

Project ini menerapkan empat operasi utama dalam database:

Create

Menambahkan data user baru ke database menggunakan SQL INSERT.

Read

Menampilkan seluruh data user atau mencari user berdasarkan ID menggunakan SQL SELECT.

Update

Mengubah nama dan email user berdasarkan ID menggunakan SQL UPDATE.

Delete

Menghapus user berdasarkan ID menggunakan SQL DELETE.

Example Menu
=== USER MANAGEMENT ===
1. Lihat semua user
2. Tambah user
3. Cari user
4. Update user
5. Hapus user
6. Keluar
Example Data

Contoh data yang terdapat di dalam database:

ID	Nama	Email
1	Falen	falen@example.com
2	Kimmy	kimmy@example.com
How to Run
1. Pastikan MySQL Berjalan

Pastikan MySQL sudah berjalan melalui Laragon atau MySQL Server.

2. Aktifkan Virtual Environment

Dari folder utama project:

.\.venv\Scripts\Activate.ps1
3. Masuk ke Folder Project
cd python-mysql
4. Install MySQL Connector

Jika library belum tersedia:

pip install mysql-connector-python
5. Jalankan Program
python app.py
Database Connection

Program menggunakan konfigurasi database berikut:

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_mysql"
)

Jika MySQL menggunakan password, bagian password dapat disesuaikan dengan password MySQL.

Learning Goals

Project ini dibuat untuk mempraktikkan beberapa konsep Python dan database, yaitu:

Python basic
Input dan output
Conditional
Loop
MySQL
Database connection
SQL
SELECT
INSERT
UPDATE
DELETE
CRUD
mysql-connector-python
Git dan GitHub
Future Development

Project ini masih dapat dikembangkan dengan beberapa fitur tambahan, seperti:

Validasi input
Pencarian berdasarkan nama
Sorting data
Sistem login
Pagination
REST API menggunakan Flask
Integrasi dengan frontend
Author

Faletehan Al Farabi

Software Engineering Student

GitHub:
https://github.com/FaletehanAlF


Setelah **save `README.md`**, jangan ubah `app.py` lagi.

Kalau sudah, bilang **`sudah`** → kita langsung lanjut **commit → push → Pull Request → me