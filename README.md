# Python Website (Flask) — Starter

A minimal Flask website with HTML templates, a contact form, and a tiny JSON API.

## Quick Start

1) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

2) Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3) Run the dev server:

   ```bash
   # Option A
   python app.py

   # Option B
   # pip install flask (already in requirements)
   # flask --app app run
   ```

4) Open your browser at http://127.0.0.1:5000

## Project Structure

```
py-flask-website/
├─ app.py
├─ requirements.txt
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  ├─ about.html
│  ├─ contact.html
│  └─ thanks.html
├─ static/
│  └─ style.css
└─ Dockerfile
```

## Production (Gunicorn)

```bash
pip install -r requirements.txt
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

## Docker (Optional)

```bash
docker build -t my-flask-site .
docker run -p 5000:5000 my-flask-site
```