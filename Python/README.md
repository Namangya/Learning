# Python — Learning Guide

This folder teaches Python in four stages. **Read this file only** — you do not need other guide files in subfolders.

---

## Who is this for?

- Complete beginners who want to learn programming  
- People moving into **data science** (charts, statistics, machine learning)  
- People who want to build **websites** with Django or Flask  

---

## Start here (choose your path)

| Your goal | Start with this file | Then |
|-----------|----------------------|------|
| **I am new to Python** | `Basics/hello.py` | Work through `Basics/Python-Notes.py` |
| **I want data science** | `DataScience/01_NumPy/numpy_starter.py` | Follow the curriculum table below |
| **I want a Django website** | `Django/manage.py` (after setup below) | [Django tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) |
| **I want a small Flask app** | `Flask/app.py` | Run it and change the routes |

---

## Progress markers (how to track yourself)

In the tables below, change the status as you learn:

| Symbol | Meaning |
|--------|---------|
| `[ ]` | Not started yet |
| `[~]` | Currently studying |
| `[x]` | Finished |

---

## Step 1 — Install Python (one time)

You need **Python 3.10 or newer** on your computer.

1. Open a terminal (Mac: Terminal app · Windows: Command Prompt or PowerShell).  
2. Go to this folder:
   ```bash
   cd path/to/Learning/Python
   ```
3. Create a virtual environment (keeps packages isolated):
   ```bash
   python -m venv venv
   ```
   > **Git note:** The `venv/` folder is listed in `.gitignore` — it is never pushed to Git. Each person creates their own after cloning.
4. Turn it on:
   - **Mac/Linux:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`
5. Install everything needed for all tracks:
   ```bash
   pip install -r requirements.txt
   ```

When you see `(venv)` at the start of your terminal line, setup worked.

### Optional — run DataScience checks

From the **repo root** (`Learning/`), you can use one shared environment instead:

```bash
cd path/to/Learning
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pytest hypothesis
pip install -r Python/requirements.txt
pytest Python/DataScience/tests -q
```

Git ignores `.venv/` and `.pytest_cache/` automatically.

---

## What’s in each folder?

```
Python/
├── Basics/          Your first programs (no extra setup)
├── DataScience/     Data analysis and machine learning
├── Django/          Full web framework
├── Flask/           Lightweight web framework
└── requirements.txt All Python packages (one list)
```

---

## Basics — Core Python

**How to run a file:** With your virtual environment on, type:

```bash
python Basics/hello.py
```

| File | What you will learn |
|------|---------------------|
| `Basics/hello.py` | Printing text to the screen |
| `Basics/Week-1.py` | Comments and text formatting |
| `Basics/fibonacci.py` | Loops |
| `Basics/Python-Notes.py` | Variables, types, strings, modules (lessons Day 1–13) |

---

## DataScience — Data analysis & machine learning

**Best for:** Working with numbers, spreadsheets, charts, and simple AI models.

**Start here:** Open `DataScience/01_NumPy/numpy_starter.py` in your editor. Each file has `# TODO:` comments — fill those in as practice.

**Optional:** For notebook-style learning, run:

```bash
jupyter notebook
```

Then open files from the `DataScience` folder in the browser.

### DataScience curriculum

| # | Topic | Folder | Status |
|---|-------|--------|--------|
| 01 | NumPy (number arrays) | `DataScience/01_NumPy/` | [ ] |
| 02 | Pandas (tables like Excel) | `DataScience/02_Pandas/` | [ ] |
| 03 | Charts & graphs | `DataScience/03_Visualization/` | [ ] |
| 04 | Statistics | `DataScience/04_Statistics/` | [ ] |
| 05 | Machine learning | `DataScience/05_MachineLearning/` | [ ] |
| 06 | Real projects | `DataScience/06_Projects/` | [ ] |

Each topic folder has:

- `*_starter.py` — exercises for you to complete  
- `*_notes.py` — examples you can read and run  

### Projects (topic 06)

| Project | File | What you build |
|---------|------|----------------|
| Iris flowers | `06_Projects/iris_analysis/iris_analysis.py` | Classify flower species from measurements |
| House prices | `06_Projects/housing_prices/housing_prices.py` | Predict home prices from features |

**Tests (optional):** `Python/DataScience/tests/` checks that lesson files exist.

---

## Django — Full web applications

| File | Purpose |
|------|---------|
| `Django/manage.py` | Control your Django project |

After setup (Step 1), try:

```bash
cd Django
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

---

## Flask — Small web apps

| File | Purpose |
|------|---------|
| `Flask/app.py` | A tiny website with two pages |

```bash
cd Flask
python app.py
```

Open http://localhost:5000 in your browser.

---

## Helpful links

- [Official Python documentation](https://docs.python.org/3/)  
- [Django documentation](https://docs.djangoproject.com/)  
- [Flask documentation](https://flask.palletsprojects.com/)
