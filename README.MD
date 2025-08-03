# 📝 Flask Basic Blog

![AWS Lightsail](https://img.shields.io/badge/Hosted%20on-AWS%20Lightsail-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?logo=flask)

A **modular Flask application** built using the **App Factory Pattern** and **Blueprints** for better scalability and maintainability. This lightweight blogging platform is perfect for learning Flask architecture or bootstrapping a more complex web app.  There is no blogging as of yet.  It='s just a fance user system at the moment.

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)

---

## ✨ Features

- 🔧 Modular Flask architecture with Factory pattern
- 📂 Blueprint-based routing
- 🧑‍💻 User authentication (login/register)
- 📝 Create, read, update, and delete blog posts
- 📦 SQLite for local development (easily replaceable with MySQL or PostgreSQL)
- 🧪 Unit testing setup

---

## 🧰 Tech Stack

| Layer       | Tools / Libraries                |
|-------------|----------------------------------|
| Frontend    | HTML, CSS, Bootstrap             |
| Backend     | Python, Flask                    |
| Auth        | Flask-Login                      |
| ORM         | SQLAlchemy                       |
| Forms       | Flask-WTF                        |
| Styling     | Bootstrap / Custom CSS           |
| Templates   | Jinja2                           |
| Deployment  | Gunicorn / Docker (optional)     |

---

## 🗂️ Project Structure
Using blueprints and going for a modular approach.  Each module has its own folder, its own blueprint, forms, templates and services.  ORginally, had everything in layers grouped by function, so a folder for routes, folder for models, folder for services.  But realized this modular approach seems to be "best practice" as suggested by the flask documentation

flask-basic-blog/<br>
├── auth/                  
<br>│   ├── __init__.py
<br>│   ├── forms.py
<br>│   ├── routes.py
<br>│   └── templates/         (Auth-specific templates)
<br>│
<br>├── blog/                  (Not working yet)
<br>│   ├── __init__.py
<br>│   ├── forms.py
<br>│   ├── routes.py
<br>│   └── templates/
<br>│
<br>├── main/                   (Main/root routes module)
<br>│   ├── __init__.py
<br>│   ├── routes.py
<br>│   └── templates/
<br>│
<br>├── migrations/            (Database migrations)
<br>│
<br>├── static/                (Static assets (CSS, JS, images)
<br>│
<br>├── templates/             (Shared/base templates)
<br>│
<br>├── config.py              (App configuration)
<br>├── run.py                 (Entry point to launch the app)
<br>├── requirements.txt       (Python dependencies)
<br>└── README.md              (Documentation)
---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/flask-basic-blog.git
cd flask-basic-blog

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 run.py
 -- OR -- 
flask run


