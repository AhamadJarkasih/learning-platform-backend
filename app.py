from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

# Data siswa
students = [
    {"id": 1, "name": "Ali", "grade": "A"},
    {"id": 2, "name": "Siti", "grade": "B"}
]

# Endpoint untuk mendapatkan semua siswa
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Endpoint untuk menambah siswa baru
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

# Endpoint untuk memperbarui data siswa
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        data = request.get_json()
        student.update(data)
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# Endpoint untuk menghapus siswa
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted"})

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Learning Platform API"


# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
