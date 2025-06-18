from flask import Flask, request, jsonify
import hashlib
import json
import os

app = Flask(__name__)
USER_FILE = 'users.json'

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    # Default admin setup
    users = {
        "localadmin": {
            "password": hashlib.sha256("LCIadminPassword".encode()).hexdigest(),
            "role": "admin"
        }
    }
    save_users(users)
    return users

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

@app.route('/register', methods=['POST'])
def register():
    users = load_users()
    data = request.json
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()
    role = data['role'].lower()

    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    if role not in ['admin', 'moderator', 'user']:
        return jsonify({"error": "Invalid role"}), 400

    users[username] = {"password": password, "role": role}
    save_users(users)
    return jsonify({"message": "Registration successful"})

@app.route('/login', methods=['POST'])
def login():
    users = load_users()
    data = request.json
    username = data['username']
    password = hashlib.sha256(data['password'].encode()).hexdigest()

    if username not in users or users[username]['password'] != password:
        return jsonify({"error": "Invalid login"}), 401

    return jsonify({"message": "Login successful", "role": users[username]['role']})

if __name__ == '__main__':
    app.run(debug=True)
