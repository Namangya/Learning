# Learning

A personal collection of code, notes, and projects built while learning databases, Python, and web development.

---

## What's in here

| Folder | Stack |
|--------|-------|
| [`Database/`](./Database/README.md) | PostgreSQL · Liquibase · Firefly |
| [`Python/`](./Python/README.md) | Python Basics · Django · Flask |
| [`WebDevelopment/`](./WebDevelopment/README.md) | HTML · CSS · JavaScript · Node.js · React |

---

## Quick start

```bash
git clone <your-repo-url>
cd Learning
```

Each folder has its own README with setup steps and file descriptions.

---

## Setup

### Python

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Node / React

```bash
npm install
npm start
```

### PostgreSQL

```bash
# macOS
brew services start postgresql

# Ubuntu
sudo systemctl start postgresql
```

### Liquibase

```bash
liquibase --defaults-file=Database/Liquibase/liquibase.properties update
```

---

## Structure

```
Learning/
├── Database/
│   ├── PostgreSQL/
│   │   ├── notes/
│   │   └── projects/
│   │       └── online-shopping-cart/
│   │           ├── sql/
│   │           └── postgresql/
│   │               └── changelog/
│   ├── Liquibase/
│   └── Firefly/
├── Python/
│   ├── Basics/
│   ├── Django/
│   └── Flask/
└── WebDevelopment/
    ├── HTML/
    ├── CSS/
    ├── JavaScript/
    ├── Node/
    └── React/
        ├── public/
        └── src/
```

---

## .gitignore covers

Python · Django · Flask · Node.js · React · PostgreSQL · Liquibase · macOS `.DS_Store`
