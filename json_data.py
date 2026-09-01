import json

users = [
    {
        "nama": "Falen",
        "umur": 16,
        "skill": "Python"
    },
    {
        "nama": "Kimmy",
        "umur": 24,
        "skill": "UI/UX"
    },
    {
        "nama": "Andi",
        "umur": 18,
        "skill": "JavaScript"
    }
]

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("Data berhasil disimpan.")