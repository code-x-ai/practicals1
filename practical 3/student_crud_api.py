from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
students = [
    {"id": 1, "name": "Aarav Sharma", "course": "BSc IT"},
    {"id": 2, "name": "Priya Patel", "course": "MSc IT"},
    {"id": 3, "name": "Rohan Mehta", "course": "BCA"}
]

# GET - Retrieve all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# GET - Retrieve a specific student by ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# POST - Add a new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = {
        "id": data["id"],
        "name": data["name"],
        "course": data["course"]
    }
    students.append(new_student)
    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    }), 201

# PUT - Update an existing student
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        # pip install flask
        if student["id"] == student_id:
            student["name"] = data["name"]
            student["course"] = data["course"]
            return jsonify({
                "message": "Student updated successfully",
                "student": student
            })
    return jsonify({"message": "Student not found"}), 404

# DELETE - Delete a student
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})
    return jsonify({"message": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
