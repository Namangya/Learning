# Python

Learning materials for Python — basics, Django, and Flask.

---

## Structure

```
Python/
├── Basics/             # Core Python syntax, notes, and exercises
├── Django/             # Django web framework projects
└── Flask/              # Flask microframework projects
```

---

## Basics

Foundational Python — no framework needed, just run with `python filename.py`.

| File | What it covers |
|------|---------------|
| `hello.py` | Hello World, basic print statements |
| `Week-1.py` | Comments, escape sequences, print formatting |
| `fibonacci.py` | Fibonacci series using a while loop |
| `Python-Notes.py` | Day-by-day notes: variables, operators, type casting, strings, input, slicing, modules |

**Topics covered in notes (Day 1–13):**
Variables · Data types · Operators · Type casting · User input · String indexing · String slicing · String methods · Modules · PIP

---

## Django

High-level Python web framework — batteries included.

| File | Purpose |
|------|---------|
| `manage.py` | Django project management CLI |
| `requirements.txt` | `django`, `psycopg2-binary` |

```bash
# Set up
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start a new project
django-admin startproject myproject

# Run dev server
python manage.py runserver

# Apply migrations
python manage.py migrate
```

---

## Flask

Lightweight Python web framework — minimal and flexible.

| File | Purpose |
|------|---------|
| `app.py` | Hello World Flask app with two routes |
| `requirements.txt` | `flask` |

```bash
# Set up
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python app.py
# → http://localhost:5000
```

---

## Resources

- [Python Docs](https://docs.python.org/3/)
- [Django Docs](https://docs.djangoproject.com/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [100 Days of Code – Python](https://www.udemy.com/course/100-days-of-code/)
