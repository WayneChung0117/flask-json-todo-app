# Example: Student System Managment - Todo List API

# Step 2: Setup Flask app
# Flask - Web framework to create API routes.
# request - To receive client data (like POST request body).
# jsonify - Converts Python dict to JSON for response.
from flask import Flask, request, jsonify

# Used to run the Flask app in the background.
from threading import Thread

#Allows Colab to expose local Flask server to public.
from pyngrok import ngrok
from dotenv import load_dotenv
import random
import json
import os

# ✅ Load .env file
load_dotenv()

# ✅ Set your ngrok authtoken securely
ngrok_token = os.getenv("NGROK_AUTH_TOKEN")
ngrok.set_auth_token(ngrok_token)

# Kills any existing ngrok tunnels, avoiding conflicts when you re-run the cell.
ngrok.kill()

# Create Flask App & Setup Port
app = Flask(__name__)          # sets up the app instance
PORT = random.randint(1025, 9999)   # Chooses a random available port from 1025–9999 to avoid port conflicts.

FILE_NAME  = "Students_test.json"

def save_students( students ):
  with open(FILE_NAME , "w") as f:
    json.dump(students, f, indent=2)

def load_students( ):
  if not os.path.exists(FILE_NAME ):
    return []
  with open(FILE_NAME , "r") as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      return []

# Root route
# When you open the base URL, it shows a welcome message.
@app.route("/")
def index():
    return "✅ Student Management from Flask V2.7"

# GET /students
# Loads and returns all students from file as JSON.
# Useful for reading data from the client side.
@app.route("/students", methods=["GET"])
def get_students():
    students = load_students( )
    print(students)

    return jsonify(students), 200

# POST /students
# Accepts id and name in JSON format.
# Adds the new student to the file and confirms addition.
@app.route("/students", methods=["POST"])
def add_student():
    students = load_students( )

    # Receive the JSON format data
    data = request.get_json()

    student = {
      "id": data["id"],
      "name": data["name"],
      "task": data["task"],
      "status": data["status"]
    }
    students.append(student)
    save_students(students)
    print("✅ Student added and saved.")

    return jsonify({"message": "✅ Student added", "student": student}), 201

@app.route("/students/<id>", methods=["PUT"])
def update_status( id ):
    students = load_students( )

    # Receive the JSON format data
    data = request.get_json()

    for s in students:
      if s["id"] == id:
        for key in data:
          s[key] = data[key]

        save_students(students)

        return jsonify({"message": "✅ Student updated", "student": s}), 200

    # If no match found
    print("❌ Student not found.")
    return jsonify({"error": "❌ Student not found"}), 404

@app.route("/students/<id>", methods=["DELETE"])
def delete_student( id ):
    students = load_students( )

    update_students = [ s for s in students if s["id"] != id ]

    if len(update_students) == len(students):
      return jsonify({"error": "❌ Student not found"}), 404

    save_students(update_students)

    return jsonify({"message": "✅ student delete", "student": update_students}), 200


# Start Flask in Background Thread
# Runs the Flask app without blocking the rest of your notebook.
def run():
    app.run(port=PORT)

Thread(target=run).start()

# ✅ Start ngrok tunnel
# Expose Public URL via ngrok
# Starts the tunnel and prints the public link so your app can be accessed from anywhere, even outside Colab.
public_url = ngrok.connect(PORT)
print("🌐 Public URL:", public_url)