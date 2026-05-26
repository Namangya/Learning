# Web Development — Learning Guide

This folder teaches how **websites** are built: structure (HTML), style (CSS), behavior (JavaScript), and modern tools (Node.js, React).

**Read this file only** — all directions live here.

---

## Who is this for?

- Beginners who want to understand how web pages work  
- Anyone preparing for front-end or full-stack development  
- No prior coding required for HTML/CSS; basic comfort helps for JavaScript  

---

## Start here (recommended order)

Follow these steps **in order**. Do not skip to React until you are comfortable with HTML and basic JavaScript.

| Step | What | First file to open | How to view it |
|------|------|-------------------|---------------|
| 1 | HTML (page structure) | `HTML/Introduction.html` | Double-click the file, or right-click → Open With → Browser |
| 2 | More HTML examples | `HTML/Example-1.html` → `Example-14.html` | Same — opens in Chrome, Firefox, Safari, etc. |
| 3 | CSS (colors, layout) | `CSS/Example-1.css` | Link it from a small HTML file, or read alongside `Introduction.html` |
| 4 | JavaScript (interactivity) | `JavaScript/Example-1.html` | Open in browser |
| 5 | Node.js (server) | `Node/app.js` | See setup below |
| 6 | React (modern UI) | `React/src/App.js` | See setup below |

---

## Progress markers

| Symbol | Meaning |
|--------|---------|
| `[ ]` | Not started |
| `[~]` | In progress |
| `[x]` | Done |

| Step | Topic | Status |
|------|-------|--------|
| 1 | HTML basics | [ ] |
| 2 | HTML examples (1–14) | [ ] |
| 3 | CSS | [ ] |
| 4 | JavaScript | [ ] |
| 5 | Node.js | [ ] |
| 6 | React | [ ] |

---

## What’s in each folder?

```
WebDevelopment/
├── HTML/         Web page structure (open .html files in a browser)
├── CSS/          Styling (colors, fonts, layout)
├── JavaScript/   Interactive examples (inside .html files)
├── Node/         Simple web server (runs on your computer)
└── React/        Modern app-style user interface
```

---

## HTML — Building blocks of every website

**No install needed.** A web browser is enough.

| File | What it teaches |
|------|-----------------|
| `HTML/Introduction.html` | Big reference: headings, links, forms, tables, images |
| `HTML/Example-1.html` … `Example-14.html` | One concept per file (lists, tables, forms, etc.) |
| `HTML/Example-1-CodeWithHarry.html` | Extra beginner example |
| `HTML/base-django-template.html` | Sample layout for Django projects |
| `HTML/index-postgresql-blog.html` | Sample blog-style page |

**Try this now:**

1. Open your file manager.  
2. Go to `WebDevelopment/HTML/`.  
3. Double-click `Introduction.html`.  
4. It should open in your default browser.

---

## CSS — Making pages look good

CSS files do not open usefully on their own. They style HTML pages.

| File | What it teaches |
|------|-----------------|
| `CSS/Example-1.css` | Colors, fonts, class selectors |
| `CSS/Example-2.css` | Flexbox (arranging items in rows/columns) |

**Practice:** Add `<link rel="stylesheet" href="../CSS/Example-1.css">` inside the `<head>` of a simple HTML file you create.

---

## JavaScript — Pages that respond to the user

Each file is an HTML page with JavaScript inside.

| Files | Topics |
|-------|--------|
| `JavaScript/Example-1.html` | Writing to the page |
| `JavaScript/Example-2.html` … `Example-11.html` | Variables, logic, DOM, events (step by step) |

Open them the same way as HTML files — in a browser.

---

## Node.js — Running code on a server

**You need:** [Node.js](https://nodejs.org/) installed (download the LTS version).

```bash
cd WebDevelopment/Node
node app.js
```

Then visit **http://localhost:3000** in your browser.

| File | Purpose |
|------|---------|
| `Node/app.js` | A minimal web server |
| `Node/package.json` | Project settings |

---

## React — Modern user interfaces

**You need:** Node.js installed.

```bash
cd WebDevelopment/React
npm install
npm start
```

Your browser should open **http://localhost:3000** automatically.

| File | Purpose |
|------|---------|
| `React/src/App.js` | Main screen component |
| `React/src/index.js` | Starts the app |
| `React/public/index.html` | Empty page where React draws the UI |

---

## Words you might see

| Term | Simple meaning |
|------|----------------|
| **HTML** | The skeleton of a web page (text, buttons, forms) |
| **CSS** | The paint and layout (colors, spacing) |
| **JavaScript** | Instructions that run in the browser |
| **Node.js** | JavaScript running on your computer as a server |
| **React** | A library to build complex pages from reusable pieces |

---

## Helpful links

- [MDN Web Docs](https://developer.mozilla.org/) — free reference for HTML, CSS, JS  
- [JavaScript.info](https://javascript.info/) — friendly JavaScript tutorials  
- [React official docs](https://react.dev/)

---

## Optional: automated checks

Folder `WebDevelopment/tests/` verifies this guide exists.

**One-time setup** (from repo root `Learning/` — only if you do not already have Python tests set up):

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pytest
```

**Run:**

```bash
pytest WebDevelopment/tests -q
```

`.venv/` and `.pytest_cache/` are in `.gitignore` — do not commit them.

---

## Git — Node projects

After `npm install` in `Node/` or `React/`, a `node_modules/` folder appears. It is **gitignored** — run `npm install` again after cloning on a new machine.
