# Basic Flask Project

A minimal Flask project with one HTML page and one health-check endpoint.

## Project Structure

```text
basic-flask-project/
  app.py
  requirements.txt
  templates/
    index.html
  static/
    css/
      style.css
```

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://localhost:5000
```

Health check:

```text
http://localhost:5000/health
```

## Run Tests

```bash
pytest
```
