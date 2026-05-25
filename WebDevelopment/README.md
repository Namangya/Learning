# Web Development

Learning materials for frontend and backend web development.

---

## Structure

```
WebDevelopment/
├── HTML/           # HTML examples and reference notes
├── CSS/            # CSS styling examples
├── JavaScript/     # Vanilla JS examples
├── Node/           # Node.js server-side starter
└── React/          # React frontend starter
    ├── public/
    └── src/
```

---

## HTML

Examples covering core HTML concepts.

| File | What it covers |
|------|---------------|
| `Introduction.html` | Full HTML reference — tags, forms, tables, links, CSS intro, JS intro |
| `Example-1.html` to `Example-14.html` | Progressive examples (headings, lists, tables, forms, images, links, frames, marquee, etc.) |
| `Example-1-CodeWithHarry.html` | Code with Harry series — Example 1 |
| `base-django-template.html` | Django base template with Bootstrap 5, FontAwesome, navbar, footer |
| `index-postgresql-blog.html` | Full styled blog post — PostgreSQL performance tuning article |

```bash
# Open any file directly in browser
open HTML/Introduction.html
```

---

## CSS

| File | What it covers |
|------|---------------|
| `Example-1.css` | Class selector, color, font-size, font-weight |
| `Example-2.css` | Flexbox layout — container and items |

---

## JavaScript

Vanilla JS examples embedded in HTML files.

| File | What it covers |
|------|---------------|
| `Example-1.html` | `document.write()`, comments |
| `Example-2.html` to `Example-11.html` | Progressive JS concepts |

---

## Node

Server-side JavaScript with Node.js.

| File | Purpose |
|------|---------|
| `app.js` | Basic HTTP server on port 3000 |
| `package.json` | Project config |

```bash
cd Node
node app.js
# → http://localhost:3000
```

---

## React

Frontend JavaScript library for building UIs.

| File | Purpose |
|------|---------|
| `src/App.js` | Root component |
| `src/index.js` | Entry point — renders App into DOM |
| `public/index.html` | HTML shell with `<div id="root">` |
| `package.json` | Dependencies: react, react-dom, react-scripts |

```bash
cd React
npm install
npm start
# → http://localhost:3000
```

---

## Resources

- [MDN Web Docs](https://developer.mozilla.org/)
- [JavaScript.info](https://javascript.info/)
- [Node.js Docs](https://nodejs.org/en/docs/)
- [React Docs](https://react.dev/)
- [Bootstrap 5](https://getbootstrap.com/)
