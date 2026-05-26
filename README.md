# Learning — Your Study Hub

Welcome. This folder is a **personal classroom** for three subjects:

| Subject | Folder | Who it is for |
|---------|--------|----------------|
| **Python** | [Python/](Python/README.md) | Anyone learning programming, data analysis, or web apps with Python |
| **Databases** | [Database/](Database/README.md) | Anyone learning SQL, building apps that use databases, or becoming a DBA |
| **Websites** | [WebDevelopment/](WebDevelopment/README.md) | Anyone learning how websites are built (HTML, CSS, JavaScript) |

You do **not** need to learn all three at once. Pick one subject and follow only that folder’s README.

---

## How to use this repo (simple steps)

1. **Clone or download** this project to your computer.
2. **Open the README** inside the subject you chose (links in the table above).
3. **Follow the “Start here” section** in that README — it tells you the exact first file to open.
4. **Mark your progress** in the README tables: `[ ]` = not started, `[~]` = working on it, `[x]` = done.

---

## Git — what does not get uploaded

The root `.gitignore` keeps local-only folders out of GitHub (or any remote):

| Ignored | Why |
|---------|-----|
| `.venv/` or `venv/` | Your Python packages — each machine creates its own |
| `.pytest_cache/` | Temporary files from running tests |
| `node_modules/` | JavaScript packages for React/Node (reinstall with `npm install`) |

After cloning, you must run the **setup steps** in the README for each subject you use. Those files are not stored in the repo.

---

## What’s inside each subject?

### Python
- **Basics** — variables, loops, your first scripts  
- **DataScience** — numbers, tables, charts, machine learning  
- **Django & Flask** — build web applications with Python  

### Database
- **Developer path** — design tables, write queries, stored procedures  
- **DBA path** — install, backup, security, performance (PostgreSQL & Oracle)  
- **Five database brands** — PostgreSQL, MySQL, Oracle, PL/SQL, SQL Server  

### Web Development
- **HTML & CSS** — structure and style of web pages  
- **JavaScript** — make pages interactive  
- **Node & React** — server and modern user interfaces  

---

## One-time setup (when a README asks for it)

| Subject | What you install | Command (run inside that folder) |
|---------|------------------|--------------------------------|
| Python | Python 3.10+ | See [Python/README.md](Python/README.md) |
| Database | A database app (e.g. PostgreSQL) | See [Database/README.md](Database/README.md) |
| Websites | Node.js (for React/Node only) | See [WebDevelopment/README.md](WebDevelopment/README.md) |

---

## Optional: run automated checks (tests)

Tests only check that lesson files exist. You can skip them while learning.

### One-time setup (from repo root)

```bash
cd path/to/Learning
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pytest hypothesis
pip install -r Python/requirements.txt
```

The `.venv` folder stays on your computer only — Git ignores it.

### Run all tests

```bash
# Still inside Learning/ with .venv activated
pytest Python/DataScience/tests Database/tests WebDevelopment/tests -q
```

| Subject | Tests folder |
|---------|----------------|
| Python (DataScience) | `Python/DataScience/tests/` |
| Database | `Database/tests/` |
| Web Development | `WebDevelopment/tests/` |

To run one subject only, e.g. `pytest Python/DataScience/tests -q`.

---

## Folder map (big picture)

```
Learning/
├── README.md              ← You are here
├── Python/README.md       ← All Python guides in one file
├── Database/README.md     ← All database guides in one file
└── WebDevelopment/README.md  ← All web guides in one file
```

Each subject keeps **one README only** — no extra guide files buried in subfolders.
