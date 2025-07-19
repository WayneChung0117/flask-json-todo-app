# Flask Student Todo List API

A simple RESTful API built with Flask to manage a list of students and their todo tasks.  
Designed to run in **Google Colab** or locally, and includes a **test client** using `requests`.

---

## 📦 Features

- ✅ Add / update / delete student tasks
- ✅ Simple JSON file storage
- ✅ RESTful API: GET, POST, PUT, DELETE
- ✅ Auto tunnel via ngrok (for external testing)
- ✅ Full test script to verify all endpoints

---

## 🚀 Installation

```bash
# 1. Clone the project
git clone https://github.com/yourusername/flask-todo-api.git
cd flask-todo-api

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Run the Flask App

```bash
python Todo_List_API.py
```

You’ll get a line like this:

```
🌐 Public URL: https://xxxxx.ngrok-free.app
```

Copy this link — it's your external API base URL.

---

## 🧪 Run the Test Script

> ⚠️ Update `BASE_URL` in `flask_api_test_client.py` with the actual ngrok URL

```bash
python flask_api_test_client.py
```

---

## 🧰 API Routes

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| GET    | `/students`           | Get all students         |
| POST   | `/students`           | Add new student task     |
| PUT    | `/students/<id>`      | Update student task      |
| DELETE | `/students/<id>`      | Delete student task      |

---

## 🔐 Notes

- Do **not** upload your personal `ngrok` token to public repositories.
- This API is for **practice/demo** purposes and does not use a database or authentication.

---

## ✅ Example Use Cases

- Personal learning and API prototyping
- Practice building and testing CRUD APIs
- Demo project for backend job applications

---

## 👤 Author

[Your Name] • [LinkedIn] • [GitHub]

---

## 📄 License

MIT License
