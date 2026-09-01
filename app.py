from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
        "id": 1,
        "nama": "Falen",
        "skill": "Python"
    },
    {
        "id": 2,
        "nama": "Kimmy",
        "skill": "UI/UX"
    }
]


@app.route("/")
def home():
    return "Python API berhasil berjalan!"


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({
        "message": "User tidak ditemukan"
    }), 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "nama": data["nama"],
        "skill": data["skill"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user["id"] == user_id:
            user["nama"] = data["nama"]
            user["skill"] = data["skill"]

            return jsonify(user)

    return jsonify({
        "message": "User tidak ditemukan"
    }), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return jsonify({
                "message": "User berhasil dihapus"
            })

    return jsonify({
        "message": "User tidak ditemukan"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)