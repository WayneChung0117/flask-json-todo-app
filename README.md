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

## ✅ Sample Test Output

> Output from running `Todo_List_API.py` and `flask_api_test_client.py`

```
🌐 Public URL: https://xxxxxxx.ngrok-free.app

🚀 Server Ping Status: 200
📢 Ping Response: ✅ Student Management from Flask V2.7

✅ POST: 201 {'message': '✅ Student added', 'student': {'id': '1', 'name': 'Alice', 'status': 'NA', 'task': 'homework'}}

✅ GET: 200 [{'id': '1', 'name': 'Alice', 'status': 'NA', 'task': 'homework'}]

✅ PUT: 200 {'message': '✅ Student updated', 'student': {'id': '1', 'name': 'Alice Updated', 'status': 'In progress', 'task': 'Prepare for exam'}}

✅ Update student - GET: 200 [{'id': '1', 'name': 'Alice Updated', 'status': 'In progress', 'task': 'Prepare for exam'}]

✅ DELETE: 200 {'message': '✅ student delete', 'student': []}

✅ Delete student - GET: 200 []
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
---

## ⚠️ Ngrok Permissions on Windows

If you're running this project locally on Windows for the first time, you may encounter this error when `pyngrok` tries to install `ngrok.exe`:

```
PermissionError: [Errno 13] Permission denied:
```

### ✅ Solutions:

1. **Run your terminal as Administrator**  
   Right-click on Command Prompt or PowerShell → “Run as administrator”

2. **Manually download ngrok**  
   - Download from: [https://ngrok.com/download](https://ngrok.com/download)  
   - Extract `ngrok.exe` to a custom path like `D:/Tools/ngrok.exe`
   - Update the script to use that path:

```python
from pyngrok import conf
pyngrok_config = conf.PyngrokConfig(ngrok_path="D:/Tools/ngrok.exe")
```

3. **Use ngrok in Google Colab**  
   This repo supports Google Colab where ngrok is automatically installed.

---

### ✅ .env and Token Safety

Store your `NGROK_AUTH_TOKEN` in a `.env` file like this:

```
NGROK_AUTH_TOKEN=your-token-here
```

Make sure `.env` is listed in `.gitignore` to avoid accidentally uploading it:

```
# .gitignore
.env
```

- Do **not** upload your personal `ngrok` token to public repositories.
- This API is for **practice/demo** purposes and does not use a database or authentication.

---

## ✅ Example Use Cases

- Personal learning and API prototyping
- Practice building and testing CRUD APIs
- Demo project for backend job applications

---

## 👤 Author

Wayne Chung

---

## 📄 License

MIT License
